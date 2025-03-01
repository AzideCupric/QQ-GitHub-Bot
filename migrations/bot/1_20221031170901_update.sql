-- upgrade --
CREATE TABLE IF NOT EXISTS "group_subscription" (
    "qq_group" BIGINT,
    "qqguild_channel" VARCHAR(255),
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "owner" VARCHAR(255) NOT NULL,
    "repo" VARCHAR(255) NOT NULL,
    "event" VARCHAR(255) NOT NULL,
    "action" JSONB,
    CONSTRAINT "uid_group_subsc_qq_grou_31d292" UNIQUE ("qq_group", "qqguild_channel", "owner", "repo", "event")
);
CREATE INDEX IF NOT EXISTS "idx_group_subsc_qq_grou_9d77e0" ON "group_subscription" ("qq_group");
CREATE INDEX IF NOT EXISTS "idx_group_subsc_qqguild_8a9fcf" ON "group_subscription" ("qqguild_channel");
CREATE INDEX IF NOT EXISTS "idx_group_subsc_owner_071a60" ON "group_subscription" ("owner", "repo", "event");;
CREATE TABLE IF NOT EXISTS "user_subscription" (
    "qq_id" BIGINT,
    "qqguild_id" VARCHAR(255),
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "owner" VARCHAR(255) NOT NULL,
    "repo" VARCHAR(255) NOT NULL,
    "event" VARCHAR(255) NOT NULL,
    "action" JSONB,
    CONSTRAINT "uid_user_subscr_qq_id_e156e2" UNIQUE ("qq_id", "qqguild_id", "owner", "repo", "event")
);
CREATE INDEX IF NOT EXISTS "idx_user_subscr_qq_id_d076c7" ON "user_subscription" ("qq_id");
CREATE INDEX IF NOT EXISTS "idx_user_subscr_qqguild_f24790" ON "user_subscription" ("qqguild_id");
CREATE INDEX IF NOT EXISTS "idx_user_subscr_owner_dce522" ON "user_subscription" ("owner", "repo", "event");;
CREATE UNIQUE INDEX "uid_group_qq_grou_50393d" ON "group" ("qq_group", "qqguild_channel");
CREATE UNIQUE INDEX "uid_user_qq_id_f630d6" ON "user" ("qq_id", "qqguild_id");
-- downgrade --
DROP INDEX "uid_group_qq_grou_50393d";
DROP INDEX "uid_user_qq_id_f630d6";
DROP TABLE IF EXISTS "group_subscription";
DROP TABLE IF EXISTS "user_subscription";
