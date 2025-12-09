import requests
import urllib.parse
from requests.exceptions import RequestException

__ENDPOINT_URL__: str = "https://cpmjbc.squareweb.app/api"

class Bubcyz:
    def __init__(self) -> None:
        self.auth_token = None

    def _check_auth(self) -> None:
        """校验是否已登录，未登录则抛出异常"""
        if not self.auth_token:
            raise PermissionError("操作失败：请先调用 login 方法完成账号登录")

    def _send_post_request(self, path: str, payload: dict = None) -> dict:
        """封装POST请求，统一处理网络异常"""
        payload = payload or {}
        try:
            url = f"{__ENDPOINT_URL__}/{path}"
            response = requests.post(url, data=payload)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            return {"ok": False, "error": f"请求异常: {str(e)}"}

    def _send_get_request(self, path: str) -> dict:
        """封装GET请求，统一处理网络异常"""
        try:
            url = f"{__ENDPOINT_URL__}/{path}"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            return {"ok": False, "error": f"请求异常: {str(e)}"}

    def login(self, email: str, password: str) -> int:
        payload = {"account_email": email, "account_password": password}
        response_decoded = self._send_post_request("account_login", payload)
        if response_decoded.get("ok"):
            self.auth_token = response_decoded.get("auth")
        return response_decoded.get("error", -1)

    def change_email(self, new_email: str) -> bool:
        self._check_auth()
        decoded_email = urllib.parse.unquote(new_email)
        payload = {
            "account_auth": self.auth_token,
            "new_email": decoded_email
        }
        response_decoded = self._send_post_request("change_email", payload)
        if response_decoded.get("new_token"):
            self.auth_token = response_decoded["new_token"]
        return response_decoded.get("ok", False)

    def change_password(self, new_password: str) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token, "new_password": new_password}
        response_decoded = self._send_post_request("change_password", payload)
        if response_decoded.get("new_token"):
            self.auth_token = response_decoded["new_token"]
        return response_decoded.get("ok", False)

    def register(self, email: str, password: str) -> int:
        payload = {"account_email": email, "account_password": password}
        response_decoded = self._send_post_request("account_register", payload)
        return response_decoded.get("error", -1)

    def delete(self) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token}
        response_decoded = self._send_post_request("account_delete", payload)
        return response_decoded.get("ok", False)

    def get_player_data(self) -> dict:
        self._check_auth()
        payload = {"account_auth": self.auth_token}
        return self._send_post_request("get_data", payload)

    def set_player_rank(self) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token}
        response_decoded = self._send_post_request("set_rank", payload)
        return response_decoded.get("ok", False)

    def get_key_data(self) -> dict:
        # 原接口依赖 access_key，移除后该方法可能失效，需根据实际接口调整
        return {"ok": False, "error": "该接口原依赖 access_key，已移除相关校验"}

    def set_player_money(self, amount: int) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token, "amount": amount}
        response_decoded = self._send_post_request("set_money", payload)
        return response_decoded.get("ok", False)

    def set_player_coins(self, amount: int) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token, "amount": amount}
        response_decoded = self._send_post_request("set_coins", payload)
        return response_decoded.get("ok", False)

    def set_player_name(self, name: str) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token, "name": name}
        response_decoded = self._send_post_request("set_name", payload)
        return response_decoded.get("ok", False)

    def set_player_localid(self, id: str) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token, "id": id}
        response_decoded = self._send_post_request("set_id", payload)
        return response_decoded.get("ok", False)

    def get_player_car(self, car_id: str) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token, "car_id": car_id}
        response_decoded = self._send_post_request("get_car", payload)
        return response_decoded.get("ok", False)

    def delete_player_friends(self) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token}
        response_decoded = self._send_post_request("delete_friends", payload)
        return response_decoded.get("ok", False)

    def unlock_w16(self) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token}
        response_decoded = self._send_post_request("unlock_w16", payload)
        return response_decoded.get("ok", False)

    def unlock_horns(self) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token}
        response_decoded = self._send_post_request("unlock_horns", payload)
        return response_decoded.get("ok", False)

    def disable_engine_damage(self) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token}
        response_decoded = self._send_post_request("disable_damage", payload)
        return response_decoded.get("ok", False)

    def unlimited_fuel(self) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token}
        response_decoded = self._send_post_request("unlimited_fuel", payload)
        return response_decoded.get("ok", False)

    def set_player_wins(self, amount: int) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token, "amount": amount}
        response_decoded = self._send_post_request("set_race_wins", payload)
        return response_decoded.get("ok", False)

    def set_player_loses(self, amount: int) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token, "amount": amount}
        response_decoded = self._send_post_request("set_race_loses", payload)
        return response_decoded.get("ok", False)

    def unlock_houses(self) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token}
        response_decoded = self._send_post_request("unlock_houses", payload)
        return response_decoded.get("ok", False)

    def unlock_smoke(self) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token}
        response_decoded = self._send_post_request("unlock_smoke", payload)
        return response_decoded.get("ok", False)

    def unlock_paid_cars(self) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token}
        response_decoded = self._send_post_request("unlock_paid_cars", payload)
        return response_decoded.get("ok", False)

    def unlock_all_cars(self) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token}
        response_decoded = self._send_post_request("unlock_all_cars", payload)
        return response_decoded.get("ok", False)

    def unlock_all_cars_siren(self) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token}
        response_decoded = self._send_post_request("unlock_all_cars_siren", payload)
        return response_decoded.get("ok", False)

    def account_clone(self, account_email: str, account_password: str) -> bool:
        self._check_auth()
        payload = {
            "account_auth": self.auth_token,
            "account_email": account_email,
            "account_password": account_password
        }
        response_decoded = self._send_post_request("clone", payload)
        return response_decoded.get("ok", False)

    def set_player_plates(self) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token}
        response_decoded = self._send_post_request("set_plates", payload)
        return response_decoded.get("ok", False)

    def unlock_wheels(self) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token}
        response_decoded = self._send_post_request("unlock_wheels", payload)
        return response_decoded.get("ok", False)

    def unlock_equipments_male(self) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token}
        response_decoded = self._send_post_request("unlock_equipments_male", payload)
        return response_decoded.get("ok", False)

    def unlock_equipments_female(self) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token}
        response_decoded = self._send_post_request("unlock_equipments_female", payload)
        return response_decoded.get("ok", False)

    def hack_car_speed(self, car_id: str, new_hp: int, new_inner_hp: int, new_nm: int, new_torque: int) -> bool:
        self._check_auth()
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "new_hp": new_hp,
            "new_inner_hp": new_inner_hp,
            "new_nm": new_nm,
            "new_torque": new_torque,
        }
        response_decoded = self._send_post_request("hack_car_speed", payload)
        return response_decoded.get("ok", False)

    def unlock_animations(self) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token}
        response_decoded = self._send_post_request("unlock_animations", payload)
        return response_decoded.get("ok", False)

    def max_max1(self, car_id: str, custom: any) -> bool:
        self._check_auth()
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        response_decoded = self._send_post_request("max_max1", payload)
        return response_decoded.get("ok", False)

    def max_max2(self, car_id: str, custom: any) -> bool:
        self._check_auth()
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        response_decoded = self._send_post_request("max_max2", payload)
        return response_decoded.get("ok", False)

    def millage_car(self, car_id: str, custom: any) -> bool:
        self._check_auth()
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        response_decoded = self._send_post_request("millage_car", payload)
        return response_decoded.get("ok", False)

    def brake_car(self, car_id: str, custom: any) -> bool:
        self._check_auth()
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        response_decoded = self._send_post_request("brake_car", payload)
        return response_decoded.get("ok", False)

    def unlock_crown(self) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token}
        response_decoded = self._send_post_request("unlock_crown", payload)
        return response_decoded.get("ok", False)

    def rear_bumper(self, car_id: str) -> bool:
        self._check_auth()
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
        }
        response_decoded = self._send_post_request("rear_bumper", payload)
        return response_decoded.get("ok", False)

    def front_bumper(self, car_id: str) -> bool:
        self._check_auth()
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
        }
        response_decoded = self._send_post_request("front_bumper", payload)
        return response_decoded.get("ok", False)

    def shittin(self) -> bool:
        self._check_auth()
        payload = {"account_auth": self.auth_token}
        response_decoded = self._send_post_request("shittin", payload)
        return response_decoded.get("ok", False)

    def testin(self, custom: any) -> bool:
        self._check_auth()
        payload = {
            "account_auth": self.auth_token,
            "custom": custom,
        }
        response_decoded = self._send_post_request("testin", payload)
        return response_decoded.get("ok", False)

    def telmunnongodz(self, car_id: str, custom: any) -> bool:
        self._check_auth()
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        response_decoded = self._send_post_request("telmunnongodz", payload)
        return response_decoded.get("ok", False)

    def telmunnongonz(self, car_id: str, custom: any) -> bool:
        self._check_auth()
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        response_decoded = self._send_post_request("telmunnongonz", payload)
        return response_decoded.get("ok", False)