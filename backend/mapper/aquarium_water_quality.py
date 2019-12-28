import sqlite3
from backend.config import get_config_by_env
from backend.model.aquarium_water_quality import (
    AquariumWaterQuality
)


class AquariumWaterQualityMapper:
    FETCH_SQL = """
        select
            measured_at,
            ph,
            temperature
        from aquarium_water_qualities
        order by measured_at asc;
    """

    @classmethod
    def find(cls):
        # if option is None:
        #     raise ValueError()
        # if not isinstance(option, AquariumWaterQualitySearchOption):
        #     raise TypeError()

        database = get_config_by_env().get_database_path()
        rows = None
        with sqlite3.connect(database, isolation_level="DEFERRED") as tran:
            tran.row_factory = sqlite3.Row
            rows = tran.execute(cls.FETCH_SQL).fetchall()
            # rows = tran.execute(cls.FETCH_SQL, vars(option)).fetchall()
        return None if rows is None else [AquariumWaterQuality(**row) for row in rows]
