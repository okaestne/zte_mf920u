import base64
import json
import logging

import zte_mf

logging.basicConfig()
log = logging.getLogger("status")

PASSWD = base64.b64encode(b"nimda1")

zte = zte_mf.ZTEMF()
l = zte.login(PASSWD)

if l.status_code != 200:
    log.error("login failed!!!")
    exit(1)

print(json.dumps(zte.get_cmd([
    "modem_main_state",
    "modem_model",
    "pin_status",
    "battery_charging",
    "battery_value",
    "sta_ip_status",
    "current_network",
    "network_type",
    "mdm_mcc",
    "mdm_mnc",
    "lac_code",
    "cell_id",
    "lte_pci",
    "lte_rsrp",
    "lte_rsrq",
    "lte_rssi",
    "lte_snr",
    "wan_active_band",
    ]).json(), indent=True))
