# Generated by Django 2.2.16 on 2021-07-27 08:48

import apps.vadmin.op_drf.fields
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
            name='QuestionBroad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', apps.vadmin.op_drf.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('update_datetime', apps.vadmin.op_drf.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', apps.vadmin.op_drf.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('question_name', models.CharField(help_text='问题大类名称', max_length=8, verbose_name='问题大类名称')),
            ],
            options={
                'verbose_name': '问题大类',
                'verbose_name_plural': '问题大类',
            },
        ),
        migrations.CreateModel(
            name='QuestionLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', apps.vadmin.op_drf.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('update_datetime', apps.vadmin.op_drf.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', apps.vadmin.op_drf.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('question_level', models.CharField(help_text='问题等级', max_length=8, verbose_name='问题等级')),
            ],
            options={
                'verbose_name': '问题等级',
                'verbose_name_plural': '问题等级',
            },
        ),
        migrations.CreateModel(
            name='QuestionOrigin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', apps.vadmin.op_drf.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('update_datetime', apps.vadmin.op_drf.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', apps.vadmin.op_drf.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('question_origin', models.CharField(help_text='问题来源', max_length=8, verbose_name='问题来源')),
            ],
            options={
                'verbose_name': '问题来源',
                'verbose_name_plural': '问题来源',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', apps.vadmin.op_drf.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', apps.vadmin.op_drf.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', apps.vadmin.op_drf.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', apps.vadmin.op_drf.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('question_title', models.CharField(help_text='问题主题', max_length=128, verbose_name='问题主题')),
                ('machine_category', models.CharField(help_text='机型类别', max_length=32, null=True, verbose_name='机型类别')),
                ('machine_name', models.CharField(help_text='机器名称', max_length=32, null=True, verbose_name='机器名称')),
                ('machine_num', models.IntegerField(help_text='涉及台数', null=True, verbose_name='涉及台数')),
                ('question_broad', models.CharField(help_text='问题大类', max_length=32, null=True, verbose_name='问题大类')),
                ('question_slender', models.CharField(help_text='问题细类', max_length=32, null=True, verbose_name='问题细类')),
                ('duty_dep_id', models.IntegerField(help_text='部门id', verbose_name='部门id')),
                ('duty_office_id', models.IntegerField(help_text='科室id', null=True, verbose_name='科室id')),
                ('duty_person', models.CharField(help_text='责任人', max_length=8, verbose_name='责任人')),
                ('occur_time', models.DateTimeField(help_text='发生时间', verbose_name='发生时间')),
                ('number', models.IntegerField(help_text='故障数量', null=True, verbose_name='故障数量')),
                ('question_level', models.CharField(help_text='重要程度', max_length=8, verbose_name='重要程度')),
                ('question_origin', models.CharField(help_text='问题来源', max_length=8, verbose_name='问题来源')),
                ('title_status', models.CharField(help_text='问题状态', max_length=8, verbose_name='问题状态')),
                ('black_point', models.CharField(help_text='黑点', max_length=8, null=True, verbose_name='黑点')),
                ('question_description', models.CharField(help_text='问题描述', max_length=128, verbose_name='问题描述')),
                ('question_schedule', models.CharField(help_text='问题进度', max_length=128, verbose_name='问题进度')),
                ('attachment', models.TextField(help_text='附件', null=True, verbose_name='附件')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
            ],
            options={
                'verbose_name': '质量管理',
                'verbose_name_plural': '质量管理',
            },
        ),
    ]
