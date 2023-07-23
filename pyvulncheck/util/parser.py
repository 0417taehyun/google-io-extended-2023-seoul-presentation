from custom import Package

class TextfileParser:
    @staticmethod
    def parse_to_dictionary(file_path: str) -> list[Package]:
        packages_information: list[Package] = []

        with open(file=file_path) as file:
            packages: list[str] = file.read().strip().split("\n")
        
        for package in packages:
            name, version = package.split("==")
            packages_information.append(Package(name=name, version=version))

        return packages_information
    