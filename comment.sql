
create table comment
(
    nickname varchar(20)  not null,
    id       varchar(30)  null,
    score    varchar(20)  null,
    content  varchar(800) null,
    data     varchar(20)  null
)
    comment '商品评论数据';

