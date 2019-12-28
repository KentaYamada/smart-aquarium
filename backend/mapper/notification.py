import sqlite3
from backend.config import get_config_by_env
from backend.model.notification import Notification


class NotificationMapper:
    FETCH_SQL = """
        select
            datetime(created_at) as created_at,
            message
        from notifications
        order by datetime(created_at) desc
        limit 20;
    """

    @classmethod
    def find(cls):
        database = get_config_by_env().get_database_path()
        rows = None
        with sqlite3.connect(database, isolation_level='DEFERRED') as tran:
            tran.row_factory = sqlite3.Row
            rows = tran.execute(cls.FETCH_SQL).fetchall()
        return None if rows is None else [Notification(**row) for row in rows]
