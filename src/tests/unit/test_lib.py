#!/usr/bin/python3


class TestLib():
    def test_pytest(self):
        assert True

    def test_radarr(self, radarr):
        ''' See if the helper fixture works to load charm configs '''
        assert isinstance(radarr.charm_config, dict)

    # Include tests for functions in lib_radarr
