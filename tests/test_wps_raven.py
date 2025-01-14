from pywps import Service
from pywps.tests import assert_response_success
from . common import client_for, TESTDATA, CFG_FILE
from raven.processes import RavenProcess

cf = ['rvi', 'rvp', 'rvc', 'rvh', 'rvt']


class TestRavenProcess:

    def test_gr4j_salmon_nc(self):
        client = client_for(Service(processes=[RavenProcess(), ], cfgfiles=CFG_FILE))

        rvs = TESTDATA['raven-gr4j-cemaneige-nc-rv']
        ts = TESTDATA['raven-gr4j-cemaneige-nc-ts']
        config = {f.suffix[1:]: f for f in rvs}

        datainputs = ("ts=files@xlink:href=file://{ts};" + ";".join(["conf=files@xlink:href=file://{%s}" % key for key
                                                                     in cf])).format(ts=ts, **config)

        resp = client.get(
            service='WPS', request='Execute', version='1.0.0', identifier='raven',
            datainputs=datainputs)

        assert_response_success(resp)

    def test_hmets(self):
        client = client_for(Service(processes=[RavenProcess(), ], cfgfiles=CFG_FILE))

        rvs = TESTDATA['raven-hmets-rv']
        ts = TESTDATA['raven-hmets-ts']
        config = {f.suffix[1:]: f for f in rvs}

        datainputs = ("ts=files@xlink:href=file://{};"
                      "ts=files@xlink:href=file://{};" + ';'.join(["conf=files@xlink:href=file://{%s}" % key for key
                                                                   in cf])).format(*ts, **config)

        resp = client.get(
            service='WPS', request='Execute', version='1.0.0', identifier='raven',
            datainputs=datainputs)
        assert_response_success(resp)

    def test_mohyse(self):
        client = client_for(Service(processes=[RavenProcess(), ], cfgfiles=CFG_FILE))

        rvs = TESTDATA['raven-mohyse-rv']
        ts = TESTDATA['raven-mohyse-ts']
        config = {f.suffix[1:]: f for f in rvs}

        datainputs = ("ts=files@xlink:href=file://{};"
                      "ts=files@xlink:href=file://{};" + ';'.join(["conf=files@xlink:href=file://{%s}" % key for key
                                                                   in cf])).format(*ts, **config)

        resp = client.get(
            service='WPS', request='Execute', version='1.0.0', identifier='raven',
            datainputs=datainputs)
        assert_response_success(resp)

    def test_hbv_ec(self):
        client = client_for(Service(processes=[RavenProcess(), ], cfgfiles=CFG_FILE))

        rvs = TESTDATA['raven-hbv-ec-rv']
        ts = TESTDATA['raven-hbv-ec-ts']
        config = {f.suffix[1:]: f for f in rvs}

        datainputs = ("ts=files@xlink:href=file://{};"
                      "ts=files@xlink:href=file://{};" + ';'.join(["conf=files@xlink:href=file://{%s}" % key for key
                                                                   in cf])).format(*ts, **config)

        resp = client.get(
            service='WPS', request='Execute', version='1.0.0', identifier='raven',
            datainputs=datainputs)
        assert_response_success(resp)
