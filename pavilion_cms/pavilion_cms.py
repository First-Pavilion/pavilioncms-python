"""Main module."""

import requests

from pavilion_cms.utils import handle_errors, handle_api_list_response


# BASE_URL = "https://api.pavilioncms.com/api/v1"

BASE_URL = "http://localhost:8000/api/v1"


class PavilionCMS:
    def __init__(self, read_token):
        self._session = requests.Session()
        self._session.headers.update({"ReadToken": read_token})
        self._session.headers.update({"Content-Type": "application/json"})
        self._session.headers.update({"Accept": "application/json"})
        self._session.headers.update({"User-Agent": "pavilioncms-python-client"})

        self._base_url = BASE_URL
        self.tag_url = f"{self._base_url}/tag"
        self.category_url = f"{self._base_url}/category"
        self.post_url = f"{self._base_url}/post"

    def get_all_tags(self, name: str = None, page: int = 1) -> dict:
        """Get all tags."""
        param = {
            "page": page,
        }
        if name:
            param.update({"name": name})

        response = self._session.get(f"{self.tag_url}/all/", params=param)

        handle_errors(response)

        return handle_api_list_response(response)

    def get_tag(self, tag_id: str) -> dict:
        """Get a tag."""
        response = self._session.get(f"{self.tag_url}/{tag_id}/view/")

        handle_errors(response)

        return response.json()

    def get_all_categories(self, name: str = None, page: int = 1) -> dict:
        param = {
            "page": page,
        }

        if name:
            param.update({"name": name})

        response = self._session.get(f"{self.category_url}/all/", params=param)

        handle_errors(response)

        return handle_api_list_response(response=response)

    def get_category(self, category_id: str) -> dict:
        response = self._session.get(f"{self.category_url}/{category_id}/view/")

        handle_errors(response)

        return response.json()

    def get_all_posts(
        self, page: int = 1, title: str = None, is_published: bool = None
    ) -> dict:
        param = {
            "page": page,
        }
        if title:
            param.update({"title": title})
        if is_published is not None:
            param.update({"is_published": is_published})

        response = self._session.get(f"{self.post_url}/all/", params=param)

        handle_errors(response)

        return handle_api_list_response(response=response)

    def get_post(self, post_id: str, post_slug: str) -> dict:
        response = self._session.get(f"{self.post_url}/{post_id}/{post_slug}/")

        handle_errors(response)

        return response.json()
