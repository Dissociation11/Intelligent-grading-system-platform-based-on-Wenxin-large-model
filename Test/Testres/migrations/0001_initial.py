# Generated by Django 4.1 on 2023-04-10 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('name', models.CharField(max_length=20, verbose_name='学院')),
            ],
            options={
                'verbose_name': '学院',
                'verbose_name_plural': '学院',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('course_id', models.CharField(max_length=10, verbose_name='课程号')),
                ('course_name', models.CharField(max_length=30, verbose_name='课程名称')),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('major', models.CharField(max_length=30, verbose_name='专业')),
                #('academy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examres.academy', verbose_name='学院')),
                ('academy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Testres.academy',
                                              verbose_name='学院')),
            ],
            options={
                'verbose_name': '专业',
                'verbose_name_plural': '专业',
            },
        ),
        migrations.CreateModel(
            name='QuestionBank',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('title', models.TextField(verbose_name='题目')),
                ('qtype', models.CharField(choices=[('单选', '单选'), ('多选', '多选'), ('判断', '判断')], max_length=40, verbose_name='题目类型')),
                ('a', models.CharField(max_length=40, verbose_name='A选项')),
                ('b', models.CharField(max_length=40, verbose_name='B选项')),
                ('c', models.CharField(max_length=40, verbose_name='C选项')),
                ('d', models.CharField(max_length=40, verbose_name='D选项')),
                ('answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=4, verbose_name='答案')),
                ('difficulty', models.CharField(choices=[('easy', '简单'), ('middle', '中等'), ('difficult', '难')], max_length=10, verbose_name='难度')),
                ('score', models.IntegerField(verbose_name='分值')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Testres.course', verbose_name='科目')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Testres.major', verbose_name='专业')),
            ],
            options={
                'verbose_name': '题库',
                'verbose_name_plural': '题库',
            },
        ),
        migrations.CreateModel(
            name='TestPaper',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('title', models.CharField(max_length=40, unique=True, verbose_name='题目')),
                ('time', models.IntegerField(help_text='单位是分钟', verbose_name='考试时长')),
                ('examtime', models.DateTimeField(verbose_name='上次考试时间')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Testres.course', verbose_name='科目')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Testres.major', verbose_name='考卷适合专业')),
                ('pid', models.ManyToManyField(to='Testres.questionbank')),
            ],
            options={
                'verbose_name': '试卷',
                'verbose_name_plural': '试卷',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='学号')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='姓名')),
                ('sex', models.BooleanField(choices=[(0, '女'), (1, '男')], verbose_name='性别')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('sclass', models.CharField(help_text='例如: 17-03', max_length=20, verbose_name='班级')),
                ('email', models.EmailField(default=None, max_length=254, verbose_name='邮箱')),
                ('pwd', models.CharField(max_length=20, verbose_name='密码')),
                ('academy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Testres.academy', verbose_name='学院')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Testres.major', verbose_name='专业')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生信息表',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('grade', models.FloatField(verbose_name='成绩')),
                ('rtime', models.DateTimeField(blank=True, null=True, verbose_name='考试时间')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stu_course', to='Testres.course', verbose_name='考试科目')),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stu_xuehao', to='Testres.student', verbose_name='学号')),
            ],
            options={
                'verbose_name': '学生成绩',
                'verbose_name_plural': '学生成绩',
            },
        ),
    ]
