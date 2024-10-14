import logging
import requests


class ZTEMF:
    def __init__(self, ip = "192.168.0.1") -> None:
        self._log = logging.getLogger("zte_mf")
        self._base_url =  f"http://{ip}/goform"
        self._headers = {
            'Referer': f"http://{ip}/index.html",
            'Host': ip
        }
        self._cookies = None

    def get_cmd(self, keys: str | list[str]):
        GET_CMD_URL = f"{self._base_url}/goform_get_cmd_process"
        params = {
            "cmd": keys if isinstance(keys, str) else ",".join(keys),
            "isTest": "false",
            "multi_data": str(int(isinstance(keys, list)))
        }

        res = requests.get(GET_CMD_URL,
                           headers=self._headers,
                           cookies=self._cookies,
                           params=params)
        self._log.debug("get %s: %d", keys, res.status_code)
        return res

    def set_cmd(self, form_id: str, params):
        SET_CMD_URL = f"{self._base_url}/goform_set_cmd_process"
        res = requests.post(SET_CMD_URL,
                            headers=self._headers,
                            cookies=self._cookies,
                            data={"goformId": form_id,
                                  "isTest": "false",
                                  **params})
        self._log.debug("form_id: %d - %s", res.status_code, res.text)
        return res

    def login(self, passwd):
        res = self.set_cmd("LOGIN", {"password": passwd})
        if res.status_code != 200:
            self._log.error("login failed! note: passwd needs to be base64 encoded")
        else:
            self._log.info("login success")
            self._cookies = res.cookies
        return res
