import os
import requests
from requests.auth import HTTPDigestAuth

# ===== 配置参数 =====
USER = "admin"
PASSWORD = "CCTV2o25W1n"
IMG_FOLDER = r"C:\code\NVR-snapshot\snapshots"
TIMEOUT = 5
# ====================

os.makedirs(IMG_FOLDER, exist_ok=True)


def create_session():
    """创建并返回一个带 Digest 认证的 Session"""
    session = requests.Session()
    session.auth = HTTPDigestAuth(USER, PASSWORD)
    session.headers.update({
        "User-Agent": "Mozilla/5.0",
        "Accept": "*/*",
        "Connection": "keep-alive"
    })
    return session


def get_nvr_snapshot(nvr_ip, channel):
    """
    从指定 NVR 的指定通道获取一张截图并保存

    文件名格式：
    nvr-{nvr_ip}-{channel}.jpg
    """
    session = create_session()

    try:
        url = f"http://{nvr_ip}/cgi-bin/snapshot.cgi?channel={channel}"
        r = session.get(url, timeout=TIMEOUT)
        r.raise_for_status()

        filename = f"nvr-{nvr_ip}-{channel}.jpg"
        filepath = os.path.join(IMG_FOLDER, filename)

        with open(filepath, "wb") as f:
            f.write(r.content)

        print(f"✅ 截图成功：{filepath}")
        return filepath

    except Exception as e:
        print(f"❌ NVR {nvr_ip} 通道 {channel} 获取失败: {e}")
        return None

    finally:
        session.close()

if __name__ == "__main__":
    nvr_list = ["10.3.132.11",
                "10.3.132.12",
                "10.3.132.13",
                "10.3.132.14",
                "10.3.132.15",
                "10.3.132.16",
                "10.3.132.17",
                "10.3.132.18",
                "10.3.132.19",
                "10.3.132.20",
                "10.3.132.21",
                "10.3.132.22",
                "10.3.132.23",
                "10.3.132.24",
                ]
    for nvr_ip in nvr_list:
        for channel in range(1, 32):
            get_nvr_snapshot(nvr_ip, channel)