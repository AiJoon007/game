
default cho_ev_talk_to_me_t1_e1 = Event(id="cho_ev_talk_to_me_t1_e1", label="cc_pf_talk_T1_intro_E1", req="states.cho.tier == 1", queue="cho_eventqueue_talk_to_me", autoenqueue=True, autodequeue=False, repeat=False)
default cho_ev_talk_to_me_t1_e2 = Event(id="cho_ev_talk_to_me_t1_e2", label="cc_pf_talk_T1_intro_E2", req="states.cho.tier == 1", queue="cho_eventqueue_talk_to_me", autoenqueue=True, autodequeue=False, repeat=False)
default cho_ev_talk_to_me_t1_e3 = Event(id="cho_ev_talk_to_me_t1_e3", label="cc_pf_talk_T1_E3", req="states.cho.tier == 1", queue="cho_eventqueue_talk_to_me", autoenqueue=True, autodequeue=False)
default cho_ev_talk_to_me_t2_e1 = Event(id="cho_ev_talk_to_me_t2_e1", label="cc_pf_talk_T2_intro_E1", req="states.cho.tier == 2", queue="cho_eventqueue_talk_to_me", autoenqueue=True, autodequeue=False, repeat=False)
default cho_ev_talk_to_me_t2_e2 = Event(id="cho_ev_talk_to_me_t2_e2", label="cc_pf_talk_T2_intro_E2", req="states.cho.tier == 2", queue="cho_eventqueue_talk_to_me", autoenqueue=True, autodequeue=False, repeat=False)
default cho_ev_talk_to_me_t2_e3 = Event(id="cho_ev_talk_to_me_t2_e3", label="cc_pf_talk_T2_E3", req="states.cho.tier == 2", queue="cho_eventqueue_talk_to_me", autoenqueue=True, autodequeue=False)
default cho_ev_talk_to_me_t3_e1 = Event(id="cho_ev_talk_to_me_t3_e1", label="cc_pf_talk_T3_intro_E1", req="states.cho.tier >= 3", queue="cho_eventqueue_talk_to_me", autoenqueue=True, autodequeue=False, repeat=False)
default cho_ev_talk_to_me_t3_e2 = Event(id="cho_ev_talk_to_me_t3_e2", label="cc_pf_talk_T3_intro_E2", req="states.cho.tier >= 3", queue="cho_eventqueue_talk_to_me", autoenqueue=True, autodequeue=False, repeat=False)
default cho_ev_talk_to_me_t3_e3 = Event(id="cho_ev_talk_to_me_t3_e3", label="cc_pf_talk_T3_E3", req="states.cho.tier >= 3", queue="cho_eventqueue_talk_to_me", autoenqueue=True, autodequeue=False)

default cho_ev_inspect_her_body_t2_e1 = Event(id="cho_ev_inspect_her_body_t2_e1", label="cc_pf_strip_T2_intro_E1", req="states.cho.tier == 2", queue="cho_eventqueue_inspect_her_body", autoenqueue=True, autodequeue=False, repeat=False)
default cho_ev_inspect_her_body_t2_e2 = Event(id="cho_ev_inspect_her_body_t2_e2", label="cc_pf_strip_T2_intro_E2", req="states.cho.tier == 2", queue="cho_eventqueue_inspect_her_body", autoenqueue=True, autodequeue=False, repeat=False)
default cho_ev_inspect_her_body_t2_e3 = Event(id="cho_ev_inspect_her_body_t2_e3", label="cc_pf_strip_T2_intro_E3", req="states.cho.tier == 2", queue="cho_eventqueue_inspect_her_body", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["cc_pf_strip_T2_E3_fail_repeat", "cc_pf_strip_T2_E3_fail"])
default cho_ev_inspect_her_body_t2_e4 = Event(id="cho_ev_inspect_her_body_t2_e4", label="cc_pf_strip_T2_E3_repeat", req="states.cho.tier == 2", queue="cho_eventqueue_inspect_her_body", autoenqueue=True, autodequeue=False)
default cho_ev_inspect_her_body_t3_e1 = Event(id="cho_ev_inspect_her_body_t3_e1", label="cc_pf_strip_T3_intro_E1", req="states.cho.tier >= 3", queue="cho_eventqueue_inspect_her_body", autoenqueue=True, autodequeue=False, repeat=False)
default cho_ev_inspect_her_body_t3_e2 = Event(id="cho_ev_inspect_her_body_t3_e2", label="cc_pf_strip_T3_intro_E2", req="states.cho.tier >= 3", queue="cho_eventqueue_inspect_her_body", autoenqueue=True, autodequeue=False, repeat=False)
default cho_ev_inspect_her_body_t3_e3 = Event(id="cho_ev_inspect_her_body_t3_e3", label="cc_pf_strip_T3_intro_E3", req="states.cho.tier >= 3", queue="cho_eventqueue_inspect_her_body", autoenqueue=True, autodequeue=False, repeat=False)
default cho_ev_inspect_her_body_t3_e4 = Event(id="cho_ev_inspect_her_body_t3_e4", label="cc_pf_strip_T3_repeat", req="states.cho.tier >= 3", queue="cho_eventqueue_inspect_her_body", autoenqueue=True, autodequeue=False)

default cho_ev_suck_it_t3_e1 = Event(id="cho_ev_suck_it_t3_e1", label="cc_pf_blowjob_T3_intro_E1", req="states.cho.tier >= 3", queue="cho_eventqueue_suck_it", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["cc_pf_blowjob_1"])
default cho_ev_suck_it_t3_e2 = Event(id="cho_ev_suck_it_t3_e2", label="cc_pf_blowjob_T3_E2", req="states.cho.tier >= 3", queue="cho_eventqueue_suck_it", autoenqueue=True, autodequeue=False)
default cho_ev_suck_it_t3_e3 = Event(id="cho_ev_suck_it_t3_e3", label="cc_pf_blowjob_T3_E3", req="states.cho.tier >= 3", queue="cho_eventqueue_suck_it", autoenqueue=True, autodequeue=False)

define cho_favors = [
    ("cho_eventqueue_talk_to_me", "Talk to me!"),
    ("cho_eventqueue_inspect_her_body", "Let me inspect you!"),
    ("cho_eventqueue_suck_it", "Suck it!"),
]
