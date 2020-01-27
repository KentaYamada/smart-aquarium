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

    SAVE_SQL = """
        INSERT INTO notifications (
            created_at,
            message
        ) VALUES (
            :created_at,
            :message
        );
    """

    @classmethod
    def find(cls):
        database = get_config_by_env().get_database_path()
        rows = None
        with sqlite3.connect(database, isolation_level='DEFERRED') as tran:
            tran.row_factory = sqlite3.Row
            rows = tran.execute(cls.FETCH_SQL).fetchall()
        return None if rows is None else [Notification(**row) for row in rows]

    @classmethod
    def save(cls, data):
        if data is None:
            raise ValueError()
        if not isinstance(data, Notification):
            raise TypeError()

        saved = False
        db_config = get_config_by_env().get_database_path()
        with sqlite3.connect(db_config, isolation_level='EXCLUSIVE') as tran:
            cur = tran.cursor()
            cur.execute(cls.SAVE_SQL, vars(data))
            saved = True if cur.rowcount > 0 else False
        return saved
