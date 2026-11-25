import pytest
import requests


# Turns into a normal pass once the node serves its API, then remove the marker
@pytest.mark.xfail(reason="pouw-node#59: the node does not serve its REST API yet",
                   raises=requests.ConnectionError)
def test_health(service):
    r = requests.get(service("node-1", 8000) + "/health", timeout=10)
    assert r.status_code == 200


@pytest.mark.xfail(reason="pouw-node#59: the node does not serve its REST API yet",
                   raises=requests.ConnectionError)
def test_manage_info(service):
    # what runs here: version, commit, branch and build time of the image
    r = requests.get(service("node-1", 8000) + "/manage/info", timeout=10)
    assert r.status_code == 200
    info = r.json()
    assert info["service"] == "pouw-node"
    assert {"version", "commit", "branch", "build_time"} <= info.keys()
