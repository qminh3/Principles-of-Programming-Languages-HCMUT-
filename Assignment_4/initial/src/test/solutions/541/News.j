.source News.java
.class public  News
.super java.lang.Object
.implements Reporter
.field title Ljava/lang/String;
.field content Ljava/lang/String;

.method public <init>(Ljava/lang/String;Ljava/lang/String;)V
.var 0 is this LNews; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is title Ljava/lang/String; from Label0 to Label1
.var 2 is content Ljava/lang/String; from Label0 to Label1
Label2:
	aload_0
	aload_2
	putfield News/content Ljava/lang/String;
	aload_0
	aload_2
	putfield News/content Ljava/lang/String;
Label3:
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LNews; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public headline()V
.var 0 is this LNews; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield News/title Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public body()V
.var 0 is this LNews; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield News/content Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
