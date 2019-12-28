import sqlite3
from backend.config import get_config_by_env
from backend.model.configuration import Configuration


class ConfigurationMapper:
    FETCH_SQL = """
        select
            ph_lower_limit,
            ph_upper_limit,
            temperature_lower_limit,
            temperature_upper_limit,
            measurement_trials
        from configurations
        where id = 1;
    """

    SAVE_SQL = """
        update configurations set
            ph_lower_limit = :ph_lower_limit,
            ph_upper_limit = :ph_upper_limit,
            temperature_lower_limit = :temperature_lower_limit,
            temperature_upper_limit = :temperature_upper_limit,
            measurement_trials = :measurement_trials
        where id = 1;
    """

    @classmethod
    def find(cls):
        database = get_config_by_env().get_database_path()
        row = None
        with sqlite3.connect(database, isolation_level="DEFERRED") as tran:
            tran.row_factory = sqlite3.Row
            row = tran.execute(cls.FETCH_SQL).fetchone()
        return Configuration(**row) if row is not None else None

    @classmethod
    def save(cls, model):
        if model is None or not isinstance(model, Configuration):
            raise ValueError('Invalid argument: model')

        database = get_config_by_env().get_database_path()
        affected = 0
        with sqlite3.connect(database, isolation_level='EXCLUSIVE') as tran:
            cur = tran.cursor()
            cur.execute(cls.SAVE_SQL, vars(model))
            affected = cur.rowcount
        return True if affected > 0 else False
