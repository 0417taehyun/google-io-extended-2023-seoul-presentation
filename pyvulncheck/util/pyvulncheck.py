from requests import Session, Response

from custom import GetVersionAPIResponse, GetAdvisioryAPIResponse

class OpenSourceInsightAPI:
    _PACKAGE_MANAGEMENT_SYSTEM: str = "pypi"
    _GET_VERSION_API_URL: str = f"https://api.deps.dev/v3alpha/systems/{_PACKAGE_MANAGEMENT_SYSTEM}"
    _GET_ADVISIORY_API_URL: str = "https://api.deps.dev/v3alpha/advisories"

    def __init__(self) -> None:
        self.session: Session = Session()

    def get_version(self, package_name: str, package_version: str) -> GetVersionAPIResponse:
        target_api_url: str = "/".join([
            OpenSourceInsightAPI._GET_VERSION_API_URL,
            "packages",
            package_name,
            "versions",
            package_version
        ])
        response: Response = self.session.get(url=target_api_url)
        if response.ok:
            return response.json()
        
        raise Exception("GET_VERSION API ERROR")
        
    def get_advisiory(self, advisory_key_id: str) -> GetAdvisioryAPIResponse:
        target_api_url: str = "/".join([OpenSourceInsightAPI._GET_ADVISIORY_API_URL, advisory_key_id])
        response: Response = self.session.get(url=target_api_url)
        if response.ok:
            return response.json()
        
        raise Exception("GET_ADVISIORY API ERROR")
    