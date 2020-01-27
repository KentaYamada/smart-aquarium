import sqlite3
from backend.config import get_config_by_env
from backend.model.water_quality import WaterQuality


class WaterQualityMapper:
    SAVE_SQL = """
        INSERT INTO water_qualities (
            measured_date,
            measured_time,
            ph,
            temperature
        ) VALUES (
            :measured_date,
            :measured_time,
            :ph,
            :temperature
        );
    """

    @classmethod
    def save(cls, data):
        if data is None:
            raise ValueError()
        if not isinstance(data, WaterQuality):
            raise TypeError()

        saved = False
        db_config = get_config_by_env().get_database_path()
        with sqlite3.connect(db_config, isolation_level='EXCLUSIVE') as tran:
            cur = tran.cursor()
            cur.execute(cls.SAVE_SQL, vars(data))
            saved = True if cur.rowcount > 0 else False
        return saved
