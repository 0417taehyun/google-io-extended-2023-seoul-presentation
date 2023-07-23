from custom import Package, Advisory, GetAdvisioryAPIResponse
from util import TextfileParser, OpenSourceInsightAPI


if __name__ == "__main__":
    _SAFE: int = 0

    target_package_manager: str = "requirements.txt"
    packages: list[Package] = TextfileParser.parse_to_dictionary(file_path=target_package_manager)

    print(f"{len(packages)}개의 패키지에 대한 취약성 검증을 시작해요.")
    print("----------")

    client: OpenSourceInsightAPI = OpenSourceInsightAPI()
    for package in packages:
        package_name: str = package.get("name")
        package_version: str = package.get("version")

        advisories: list[Advisory] = (
            client
            .get_version(package_name=package_name, package_version=package_version)
            .get("advisoryKeys")
        )
        for advisory in advisories:
            
            advisory_information: GetAdvisioryAPIResponse = client.get_advisiory(advisory_key_id=advisory.get("id"))
            score: int = advisory_information.get("cvss3Score")
            if score > _SAFE:
                title: str = advisory_information.get("title")
                url: str = advisory_information.get("url")
                print(f"{package_name} 패키지의 {package_version} 버전에서 {title} 취약성이 발견 되었고, 취약성 점수는 {score}/10점이에요!")
                print()
                print(f"자세한 내용은 {url}을 방문하여 확인해주세요.")
                print("----------")

    print(f"{len(packages)}개의 패키지에 대한 취약성 검증이 종료 되었어요.")
                