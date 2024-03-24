# Imperius Curse

default ast_ev_imperio_training_t1_e1 = Event(id="ast_ev_imperio_training_t1_e1", label="ag_st_imperio_E1", req="game.daytime==False")
default ast_ev_imperio_training_t1_e2 = Event(id="ast_ev_imperio_training_t1_e2", label="ag_st_imperio_E2", req="game.daytime==False")
default ast_ev_imperio_training_t1_e3 = Event(id="ast_ev_imperio_training_t1_e3", label="ag_st_imperio_E3", req="game.daytime==False")
default ast_ev_imperio_training_t1_e4 = Event(id="ast_ev_imperio_training_t1_e4", label="ag_st_imperio_E4", req="game.daytime==False")
default ast_ev_imperio_training_t1_e5 = Event(id="ast_ev_imperio_training_t1_e5", label="ag_st_imperio_E5", req="game.daytime==False")

default ast_ev_imperio_training_t1_e1_hub = Event(id="ast_ev_imperio_training_t1_e1_hub", label="ag_st_imperio", req="states.ast.tier >= 1", queue="ast_eventqueue_imperio_training_tonks", autoenqueue=True, autodequeue=False, subevents=["ast_ev_imperio_training_t1_e1"])
default ast_ev_imperio_training_t1_e2_hub = Event(id="ast_ev_imperio_training_t1_e2_hub", label="ag_st_imperio", req="states.ast.tier >= 1", queue="ast_eventqueue_imperio_training_tonks", autoenqueue=True, autodequeue=False, subevents=["ast_ev_imperio_training_t1_e2"])
default ast_ev_imperio_training_t1_e3_hub = Event(id="ast_ev_imperio_training_t1_e3_hub", label="ag_st_imperio", req="states.ast.tier >= 1", queue="ast_eventqueue_imperio_training_tonks", autoenqueue=True, autodequeue=False, subevents=["ast_ev_imperio_training_t1_e3"])
default ast_ev_imperio_training_t1_e4_hub = Event(id="ast_ev_imperio_training_t1_e4_hub", label="ag_st_imperio", req="states.ast.tier >= 1", queue="ast_eventqueue_imperio_training_tonks", autoenqueue=True, autodequeue=False, subevents=["ast_ev_imperio_training_t1_e4"])
default ast_ev_imperio_training_t1_e5_hub = Event(id="ast_ev_imperio_training_t1_e5_hub", label="ag_st_imperio", req="states.ast.tier >= 1", queue="ast_eventqueue_imperio_training_tonks", autoenqueue=True, autodequeue=False, subevents=["ast_ev_imperio_training_t1_e5"])

default ast_ev_imperio_training_susan_t1_e1 = Event(id="ast_ev_imperio_training_susan_t1_e1", label="ag_se_imperio_sb_E1", req="states.ast.tier >= 1", queue="ast_eventqueue_imperio_training_susan", autoenqueue=True, autodequeue=False)
default ast_ev_imperio_training_susan_t1_e2 = Event(id="ast_ev_imperio_training_susan_t1_e2", label="ag_se_imperio_sb_E2", req="states.ast.tier >= 1", queue="ast_eventqueue_imperio_training_susan", autoenqueue=True, autodequeue=False)
default ast_ev_imperio_training_susan_t1_e3 = Event(id="ast_ev_imperio_training_susan_t1_e3", label="ag_se_imperio_sb_E3", req="states.ast.tier >= 1", queue="ast_eventqueue_imperio_training_susan", autoenqueue=True, autodequeue=False)

define astoria_spells = [
    ("ast_eventqueue_imperio_training_tonks", "Im-perv-ious with Tonks!"),
    ("ast_eventqueue_imperio_training_susan", "Im-perv-ious with Susan!"),
]