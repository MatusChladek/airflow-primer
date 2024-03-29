import logging

from airflow.models import BaseOperator
from airflow.plugins_manager import AirflowPlugin
from airflow.utils.decorators import apply_defaults

log = logging.getLogger(__name__)


class TestOperator(BaseOperator):

    @apply_defaults
    def __init__(self, my_ope, my_operator_param, *args, **kwargs):
        self.operator_param = my_operator_param
        super(TestOperator, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info("Hello World!")
        log.info('operator param %s', self.operator_param)


class TestPlugin(AirflowPlugin):
    name = "test_plugin"
    operators = [TestOperator]
