# Generated by Django 2.2.16 on 2021-07-07 16:24

import apps.vadmin.op_drf.fields
import apps.vadmin.system.models.save_file
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DictData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', apps.vadmin.op_drf.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', apps.vadmin.op_drf.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', apps.vadmin.op_drf.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', apps.vadmin.op_drf.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('dictName', models.CharField(max_length=64, verbose_name='字典名称')),
                ('dictType', models.CharField(max_length=64, verbose_name='字典类型')),
                ('status', models.CharField(max_length=8, verbose_name='字典状态')),
                ('remark', models.CharField(blank=True, max_length=256, null=True, verbose_name='备注')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
            ],
            options={
                'verbose_name': '字典管理',
                'verbose_name_plural': '字典管理',
            },
        ),
        migrations.CreateModel(
            name='MessagePush',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', apps.vadmin.op_drf.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', apps.vadmin.op_drf.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', apps.vadmin.op_drf.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', apps.vadmin.op_drf.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('title', models.CharField(max_length=128, verbose_name='通知标题')),
                ('content', models.TextField(verbose_name='通知内容')),
                ('message_type', models.CharField(max_length=8, verbose_name='通知类型')),
                ('is_reviewed', models.BooleanField(default=True, verbose_name='是否审核')),
                ('status', models.CharField(max_length=8, verbose_name='通知状态')),
                ('to_path', models.CharField(blank=True, max_length=256, null=True, verbose_name='跳转路径')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
            ],
            options={
                'verbose_name': '通知公告',
                'verbose_name_plural': '通知公告',
            },
        ),
        migrations.CreateModel(
            name='SaveFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', apps.vadmin.op_drf.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', apps.vadmin.op_drf.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', apps.vadmin.op_drf.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', apps.vadmin.op_drf.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('name', models.CharField(blank=True, max_length=128, null=True, verbose_name='文件名称')),
                ('type', models.CharField(blank=True, max_length=200, null=True, verbose_name='文件类型')),
                ('size', models.CharField(blank=True, max_length=64, null=True, verbose_name='文件大小')),
                ('address', models.CharField(blank=True, max_length=16, null=True, verbose_name='存储位置')),
                ('source', models.CharField(blank=True, max_length=16, null=True, verbose_name='文件来源')),
                ('oss_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='OSS地址')),
                ('status', models.BooleanField(default=True, verbose_name='文件是否存在')),
                ('file', models.FileField(upload_to=apps.vadmin.system.models.save_file.files_path, verbose_name='文件URL')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
            ],
            options={
                'verbose_name': '文件管理',
                'verbose_name_plural': '文件管理',
            },
        ),
        migrations.CreateModel(
            name='OperationLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', apps.vadmin.op_drf.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', apps.vadmin.op_drf.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', apps.vadmin.op_drf.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', apps.vadmin.op_drf.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('request_modular', models.CharField(blank=True, max_length=64, null=True, verbose_name='请求模块')),
                ('request_path', models.CharField(blank=True, max_length=400, null=True, verbose_name='请求地址')),
                ('request_body', models.TextField(blank=True, null=True, verbose_name='请求参数')),
                ('request_method', models.CharField(blank=True, max_length=64, null=True, verbose_name='请求方式')),
                ('request_msg', models.TextField(blank=True, null=True, verbose_name='操作说明')),
                ('request_ip', models.CharField(blank=True, max_length=32, null=True, verbose_name='请求ip地址')),
                ('request_browser', models.CharField(blank=True, max_length=64, null=True, verbose_name='请求浏览器')),
                ('response_code', models.CharField(blank=True, max_length=32, null=True, verbose_name='响应状态码')),
                ('request_location', models.CharField(blank=True, max_length=64, null=True, verbose_name='操作地点')),
                ('request_os', models.CharField(blank=True, max_length=64, null=True, verbose_name='操作系统')),
                ('json_result', models.TextField(blank=True, null=True, verbose_name='返回信息')),
                ('status', models.BooleanField(default=False, verbose_name='响应状态')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
            ],
            options={
                'verbose_name': '操作日志',
                'verbose_name_plural': '操作日志',
            },
        ),
        migrations.CreateModel(
            name='MessagePushUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_read', models.BooleanField(default=False, verbose_name='是否已读')),
                ('update_datetime', apps.vadmin.op_drf.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', apps.vadmin.op_drf.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('message_push', models.ForeignKey(db_constraint=False, help_text='消息通知', on_delete=django.db.models.deletion.CASCADE, related_name='messagepushuser_message_push', to='system.MessagePush', verbose_name='消息通知')),
                ('user', models.ForeignKey(db_constraint=False, help_text='用户', on_delete=django.db.models.deletion.CASCADE, related_name='messagepushuser_user', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '通知公告与用户关系',
                'verbose_name_plural': '通知公告与用户关系',
            },
        ),
        migrations.AddField(
            model_name='messagepush',
            name='user',
            field=models.ManyToManyField(related_name='user', related_query_name='user_query', through='system.MessagePushUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='LoginInfor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', apps.vadmin.op_drf.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', apps.vadmin.op_drf.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', apps.vadmin.op_drf.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', apps.vadmin.op_drf.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('session_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='会话标识')),
                ('browser', models.CharField(max_length=64, verbose_name='浏览器')),
                ('ipaddr', models.CharField(blank=True, max_length=32, null=True, verbose_name='ip地址')),
                ('loginLocation', models.CharField(blank=True, max_length=64, null=True, verbose_name='登录位置')),
                ('msg', models.TextField(blank=True, null=True, verbose_name='操作信息')),
                ('os', models.CharField(blank=True, max_length=64, null=True, verbose_name='操作系统')),
                ('status', models.BooleanField(default=False, verbose_name='登录状态')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
            ],
            options={
                'verbose_name': '登录日志',
                'verbose_name_plural': '登录日志',
            },
        ),
        migrations.CreateModel(
            name='DictDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', apps.vadmin.op_drf.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', apps.vadmin.op_drf.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', apps.vadmin.op_drf.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', apps.vadmin.op_drf.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('dictLabel', models.CharField(max_length=64, verbose_name='字典标签')),
                ('dictValue', models.CharField(max_length=256, verbose_name='字典键值')),
                ('is_default', models.BooleanField(default=False, verbose_name='是否默认')),
                ('status', models.CharField(max_length=2, verbose_name='字典状态')),
                ('sort', models.CharField(max_length=256, verbose_name='字典排序')),
                ('remark', models.CharField(blank=True, max_length=256, null=True, verbose_name='备注')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('dict_data', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='system.DictData', verbose_name='关联字典')),
            ],
            options={
                'verbose_name': '字典详情',
                'verbose_name_plural': '字典详情',
            },
        ),
        migrations.CreateModel(
            name='ConfigSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', apps.vadmin.op_drf.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', apps.vadmin.op_drf.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', apps.vadmin.op_drf.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', apps.vadmin.op_drf.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('configName', models.CharField(max_length=64, verbose_name='参数名称')),
                ('configKey', models.CharField(max_length=256, verbose_name='参数键名')),
                ('configValue', models.CharField(max_length=256, verbose_name='参数键值')),
                ('configType', models.CharField(max_length=8, verbose_name='是否内置')),
                ('status', models.CharField(max_length=8, verbose_name='参数状态')),
                ('remark', models.CharField(blank=True, max_length=256, null=True, verbose_name='备注')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
            ],
            options={
                'verbose_name': '参数设置',
                'verbose_name_plural': '参数设置',
            },
        ),
        migrations.CreateModel(
            name='CeleryLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', apps.vadmin.op_drf.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', apps.vadmin.op_drf.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', apps.vadmin.op_drf.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', apps.vadmin.op_drf.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('name', models.CharField(help_text='任务名称', max_length=256, verbose_name='任务名称')),
                ('func_name', models.CharField(help_text='执行函数名称', max_length=256, verbose_name='执行函数名称')),
                ('kwargs', models.TextField(help_text='运行参数', max_length=1024, verbose_name='执行参数')),
                ('seconds', models.CharField(max_length=8, verbose_name='执行时间')),
                ('status', models.BooleanField(default=False, verbose_name='运行状态')),
                ('result', models.TextField(help_text='任务返回内容', max_length=10240, verbose_name='任务结果')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
            ],
            options={
                'verbose_name': 'celery定时日志',
                'verbose_name_plural': 'celery定时日志',
            },
        ),
    ]
