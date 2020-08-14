from tba import user as p


def test_register_participant():
    user_id = p.register_user(user_name="test_user_1")
    participant = p.get_user(user_id)

    assert participant.user_id == user_id
    assert participant.user_name == "test_user_1"
