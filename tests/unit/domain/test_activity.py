import domain.activity as activity

class TestRun():
    def test_get_name(self):
        act = activity.Run()

        assert 'run' == act.get_name()

class TestWalk():
    def test_get_name(self):
        act = activity.Walk()

        assert 'walk' == act.get_name()
