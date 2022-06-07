Server [localhost]: localhost
Database [postgres]: photos
Port [5432]: 5432
Username [postgres]: sviatlana
Password for user sviatlana:
psql (14.3)
WARNING: Console code page (866) differs from Windows code page (1251)
         8-bit characters might not work correctly. See psql reference
         page "Notes for Windows users" for details.
Type "help" for help.

photos=> CREATE TABLE IF NOT EXISTS roles(id BIGSERIAL PRIMARY KEY, role VARCHAR(255) UNIQUE);
CREATE TABLE
photos=> CREATE TABLE IF NOT EXISTS dialogs(id BIGSERIAL PRIMARY KEY, name VARCHAR(255), time_creation TIMESTAMP);
CREATE TABLE
photos=> CREATE TABLE IF NOT EXISTS users(id BIGSERIAL PRIMARY KEY, email VARCHAR(255) UNIQUE NOT NULL, password VARCHAR(64) NOT NULL, name VARCHAR(255), time_registration TIMESTAMP  now());
ОШИБКА:  ошибка синтаксиса (примерное положение: "now")
LINE 1: ...ULL, name VARCHAR(255), time_registration TIMESTAMP  now());
                                                                ^
photos=> CREATE TABLE IF NOT EXISTS users(id BIGSERIAL PRIMARY KEY, email VARCHAR(255) UNIQUE NOT NULL, password VARCHAR(64) NOT NULL, name VARCHAR(255), time_registration TIMESTAMP now());
ОШИБКА:  ошибка синтаксиса (примерное положение: "now")
LINE 1: ...NULL, name VARCHAR(255), time_registration TIMESTAMP now());
                                                                ^
photos=> CREATE TABLE IF NOT EXISTS users(id BIGSERIAL PRIMARY KEY, email VARCHAR(255) UNIQUE NOT NULL, password VARCHAR(64) NOT NULL, name VARCHAR(255), time_registration TIMESTAMP DEFAULT now());
CREATE TABLE
photos=>  CREATE TABLE IF NOT EXISTS tags(id BIGSERIAL PRIMARY KEY, name VARCHAR(50) NOT NULL);
CREATE TABLE
photos=>  CREATE TABLE IF NOT EXISTS users_to_dialogs(user_id BIGSERIAL, dialog_id  BIGSERIAL, time_creation TIMESTAMP, FOREIGN KEY (user_id) REFERENCES users(id), FOREIGN KEY (dialog_id) REFERENCES dialogs(id));
CREATE TABLE
photos=> CREATE TABLE IF NOT EXISTS users_to_roles(user_id BIGSERIAL, role_id  BIGSERIAL, FOREIGN KEY (user_id) REFERENCES users(id), FOREIGN KEY (role_id) REFERENCES roles(id));
CREATE TABLE
photos=> CREATE TABLE IF NOT EXISTS friends(user1_id BIGSERIAL, user2_id  BIGSERIAL, time_creation TIMESTAMP, FOREIGN KEY (user1_id) REFERENCES users(id), FOREIGN KEY (user2_id) REFERENCES users(id));
CREATE TABLE
photos=> CREATE TABLE IF NOT EXISTS albums(id BIGSERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, user_id BIGSERIAL, time_creation TIMESTAMP DEFAULT now(), FOREIGN KEY (user_id) REFERENCES users(id));
CREATE TABLE
photos=> CREATE TABLE IF NOT EXISTS messages(id BIGSERIAL PRIMARY KEY, dialog_id  BIGSERIAL, user_id BIGSERIAL, text TEXT, time_creation TIMESTAMP DEFAULT now(), text_changed BOOLEAN, FOREIGN KEY (user_id) REFERENCES users(id), FOREIGN KEY (dialog_id) REFERENCES dialogs(id));
CREATE TABLE
photos=> CREATE TABLE IF NOT EXISTS photos(id  BIGSERIAL PRIMARY KEY, path VARCHAR(255) NOT NULL, description  VARCHAR(255), album_id BIGSERIAL, time_creation TIMESTAMP, FOREIGN KEY (album_id) REFERENCES albums(id));
CREATE TABLE
photos=> CREATE TABLE IF NOT EXISTS tags_to_photos(photo_id BIGSERIAL, tag_id  BIGSERIAL, FOREIGN KEY (photo_id) REFERENCES photos(id), FOREIGN KEY (tag_id) REFERENCES tags(id));
CREATE TABLE
photos=> CREATE TABLE IF NOT EXISTS messages_to_photos(photo_id BIGSERIAL, message_id  BIGSERIAL, FOREIGN KEY (message_id) REFERENCES messages(id), FOREIGN KEY (photo_id) REFERENCES photos(id));
CREATE TABLE
photos=> \dt
                List of relations
 Schema |        Name        | Type  |   Owner
--------+--------------------+-------+-----------
 public | albums             | table | sviatlana
 public | dialogs            | table | sviatlana
 public | friends            | table | sviatlana
 public | messages           | table | sviatlana
 public | messages_to_photos | table | sviatlana
 public | photos             | table | sviatlana
 public | roles              | table | sviatlana
 public | tags               | table | sviatlana
 public | tags_to_photos     | table | sviatlana
 public | users              | table | sviatlana
 public | users_to_dialogs   | table | sviatlana
 public | users_to_roles     | table | sviatlana
(12 rows)


photos=> \d albums
                                            Table "public.albums"
    Column     |            Type             | Collation | Nullable |                 Default
---------------+-----------------------------+-----------+----------+-----------------------------------------
 id            | bigint                      |           | not null | nextval('albums_id_seq'::regclass)
 name          | character varying(255)      |           | not null |
 user_id       | bigint                      |           | not null | nextval('albums_user_id_seq'::regclass)
 time_creation | timestamp without time zone |           |          | now()
Indexes:
    "albums_pkey" PRIMARY KEY, btree (id)
Foreign-key constraints:
    "albums_user_id_fkey" FOREIGN KEY (user_id) REFERENCES users(id)
Referenced by:
    TABLE "photos" CONSTRAINT "photos_album_id_fkey" FOREIGN KEY (album_id) REFERENCES albums(id)


photos=> \d dialogs
                                          Table "public.dialogs"
    Column     |            Type             | Collation | Nullable |               Default
---------------+-----------------------------+-----------+----------+-------------------------------------
 id            | bigint                      |           | not null | nextval('dialogs_id_seq'::regclass)
 name          | character varying(255)      |           |          |
 time_creation | timestamp without time zone |           |          |
Indexes:
    "dialogs_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "messages" CONSTRAINT "messages_dialog_id_fkey" FOREIGN KEY (dialog_id) REFERENCES dialogs(id)
    TABLE "users_to_dialogs" CONSTRAINT "users_to_dialogs_dialog_id_fkey" FOREIGN KEY (dialog_id) REFERENCES dialogs(id)


photos=> \d friends
                                             Table "public.friends"
    Column     |            Type             | Collation | Nullable |                  Default
---------------+-----------------------------+-----------+----------+-------------------------------------------
 user1_id      | bigint                      |           | not null | nextval('friends_user1_id_seq'::regclass)
 user2_id      | bigint                      |           | not null | nextval('friends_user2_id_seq'::regclass)
 time_creation | timestamp without time zone |           |          |
Foreign-key constraints:
    "friends_user1_id_fkey" FOREIGN KEY (user1_id) REFERENCES users(id)
    "friends_user2_id_fkey" FOREIGN KEY (user2_id) REFERENCES users(id)


photos=> \d messages
                                             Table "public.messages"
    Column     |            Type             | Collation | Nullable |                   Default
---------------+-----------------------------+-----------+----------+---------------------------------------------
 id            | bigint                      |           | not null | nextval('messages_id_seq'::regclass)
 dialog_id     | bigint                      |           | not null | nextval('messages_dialog_id_seq'::regclass)
 user_id       | bigint                      |           | not null | nextval('messages_user_id_seq'::regclass)
 text          | text                        |           |          |
 time_creation | timestamp without time zone |           |          | now()
 text_changed  | boolean                     |           |          |
Indexes:
    "messages_pkey" PRIMARY KEY, btree (id)
Foreign-key constraints:
    "messages_dialog_id_fkey" FOREIGN KEY (dialog_id) REFERENCES dialogs(id)
    "messages_user_id_fkey" FOREIGN KEY (user_id) REFERENCES users(id)
Referenced by:
    TABLE "messages_to_photos" CONSTRAINT "messages_to_photos_message_id_fkey" FOREIGN KEY (message_id) REFERENCES messages(id)


photos=> \d messages_to_photos
                                  Table "public.messages_to_photos"
   Column   |  Type  | Collation | Nullable |                        Default
------------+--------+-----------+----------+--------------------------------------------------------
 photo_id   | bigint |           | not null | nextval('messages_to_photos_photo_id_seq'::regclass)
 message_id | bigint |           | not null | nextval('messages_to_photos_message_id_seq'::regclass)
Foreign-key constraints:
    "messages_to_photos_message_id_fkey" FOREIGN KEY (message_id) REFERENCES messages(id)
    "messages_to_photos_photo_id_fkey" FOREIGN KEY (photo_id) REFERENCES photos(id)


photos=> \d photos
                                             Table "public.photos"
    Column     |            Type             | Collation | Nullable |                 Default
---------------+-----------------------------+-----------+----------+------------------------------------------
 id            | bigint                      |           | not null | nextval('photos_id_seq'::regclass)
 path          | character varying(255)      |           | not null |
 description   | character varying(255)      |           |          |
 album_id      | bigint                      |           | not null | nextval('photos_album_id_seq'::regclass)
 time_creation | timestamp without time zone |           |          |
Indexes:
    "photos_pkey" PRIMARY KEY, btree (id)
Foreign-key constraints:
    "photos_album_id_fkey" FOREIGN KEY (album_id) REFERENCES albums(id)
Referenced by:
    TABLE "messages_to_photos" CONSTRAINT "messages_to_photos_photo_id_fkey" FOREIGN KEY (photo_id) REFERENCES photos(id)
    TABLE "tags_to_photos" CONSTRAINT "tags_to_photos_photo_id_fkey" FOREIGN KEY (photo_id) REFERENCES photos(id)


photos=> \d roles
                                    Table "public.roles"
 Column |          Type          | Collation | Nullable |              Default
--------+------------------------+-----------+----------+-----------------------------------
 id     | bigint                 |           | not null | nextval('roles_id_seq'::regclass)
 role   | character varying(255) |           |          |
Indexes:
    "roles_pkey" PRIMARY KEY, btree (id)
    "roles_role_key" UNIQUE CONSTRAINT, btree (role)
Referenced by:
    TABLE "users_to_roles" CONSTRAINT "users_to_roles_role_id_fkey" FOREIGN KEY (role_id) REFERENCES roles(id)


photos=> \d tags
                                   Table "public.tags"
 Column |         Type          | Collation | Nullable |             Default
--------+-----------------------+-----------+----------+----------------------------------
 id     | bigint                |           | not null | nextval('tags_id_seq'::regclass)
 name   | character varying(50) |           | not null |
Indexes:
    "tags_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "tags_to_photos" CONSTRAINT "tags_to_photos_tag_id_fkey" FOREIGN KEY (tag_id) REFERENCES tags(id)


photos=> \d tags_to_photos
                                Table "public.tags_to_photos"
  Column  |  Type  | Collation | Nullable |                     Default
----------+--------+-----------+----------+--------------------------------------------------
 photo_id | bigint |           | not null | nextval('tags_to_photos_photo_id_seq'::regclass)
 tag_id   | bigint |           | not null | nextval('tags_to_photos_tag_id_seq'::regclass)
Foreign-key constraints:
    "tags_to_photos_photo_id_fkey" FOREIGN KEY (photo_id) REFERENCES photos(id)
    "tags_to_photos_tag_id_fkey" FOREIGN KEY (tag_id) REFERENCES tags(id)


photos=> \d users
                                            Table "public.users"
      Column       |            Type             | Collation | Nullable |              Default
-------------------+-----------------------------+-----------+----------+-----------------------------------
 id                | bigint                      |           | not null | nextval('users_id_seq'::regclass)
 email             | character varying(255)      |           | not null |
 password          | character varying(64)       |           | not null |
 name              | character varying(255)      |           |          |
 time_registration | timestamp without time zone |           |          | now()
Indexes:
    "users_pkey" PRIMARY KEY, btree (id)
    "users_email_key" UNIQUE CONSTRAINT, btree (email)
Referenced by:
    TABLE "albums" CONSTRAINT "albums_user_id_fkey" FOREIGN KEY (user_id) REFERENCES users(id)
    TABLE "friends" CONSTRAINT "friends_user1_id_fkey" FOREIGN KEY (user1_id) REFERENCES users(id)
    TABLE "friends" CONSTRAINT "friends_user2_id_fkey" FOREIGN KEY (user2_id) REFERENCES users(id)
    TABLE "messages" CONSTRAINT "messages_user_id_fkey" FOREIGN KEY (user_id) REFERENCES users(id)
    TABLE "users_to_dialogs" CONSTRAINT "users_to_dialogs_user_id_fkey" FOREIGN KEY (user_id) REFERENCES users(id)
    TABLE "users_to_roles" CONSTRAINT "users_to_roles_user_id_fkey" FOREIGN KEY (user_id) REFERENCES users(id)


photos=> \d user_to_dialogs
Did not find any relation named "user_to_dialogs".
photos=> \d users_to_dialogs
                                             Table "public.users_to_dialogs"
    Column     |            Type             | Collation | Nullable |                       Default
---------------+-----------------------------+-----------+----------+-----------------------------------------------------
 user_id       | bigint                      |           | not null | nextval('users_to_dialogs_user_id_seq'::regclass)
 dialog_id     | bigint                      |           | not null | nextval('users_to_dialogs_dialog_id_seq'::regclass)
 time_creation | timestamp without time zone |           |          |
Foreign-key constraints:
    "users_to_dialogs_dialog_id_fkey" FOREIGN KEY (dialog_id) REFERENCES dialogs(id)
    "users_to_dialogs_user_id_fkey" FOREIGN KEY (user_id) REFERENCES users(id)


photos=> \d users_to_roles
                               Table "public.users_to_roles"
 Column  |  Type  | Collation | Nullable |                     Default
---------+--------+-----------+----------+-------------------------------------------------
 user_id | bigint |           | not null | nextval('users_to_roles_user_id_seq'::regclass)
 role_id | bigint |           | not null | nextval('users_to_roles_role_id_seq'::regclass)
Foreign-key constraints:
    "users_to_roles_role_id_fkey" FOREIGN KEY (role_id) REFERENCES roles(id)
    "users_to_roles_user_id_fkey" FOREIGN KEY (user_id) REFERENCES users(id)


photos=>