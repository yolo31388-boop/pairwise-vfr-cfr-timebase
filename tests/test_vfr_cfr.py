import pytest
import av.vfr_cfr as mod

CASES = [
    ("rational_timebase", (1,)),
    ("display_order_rebuild", (1,)),
    ("motion_aware_drop", (1,)),
    ("av_shared_clock", (1,)),
    ("duration_cache_reclaim", (1,)),
    ("seek_state_reset", (1,)),
    ("load_vfr", (1,)),
    ("normalize_vfr", (1,)),
    ("encode_cfr", (1,)),
    ("present_vfr", (1,)),
    ("validate_vfr", (1,)),
    ("metrics_vfr", (1,)),
    ("audit_vfr", (1,)),
    ("fallback_vfr", (1,)),
    ("determinism_vfr", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
