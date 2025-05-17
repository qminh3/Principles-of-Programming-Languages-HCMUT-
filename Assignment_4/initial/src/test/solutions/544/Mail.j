.source Mail.java
.class public  Mail
.super java.lang.Object
.implements Message
.field content Ljava/lang/String;

.method public <init>(Ljava/lang/String;)V
.var 0 is this LMail; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is content Ljava/lang/String; from Label0 to Label1
Label2:
	aload_0
	aload_1
	putfield Mail/content Ljava/lang/String;
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMail; from Label0 to Label1
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

.method public show()V
.var 0 is this LMail; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Mail/content Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public update()V
.var 0 is this LMail; from Label0 to Label1
Label0:
Label2:
.var 1 is updated LMail; from Label2 to Label3
	new Mail
	dup
	ldc "Updated content"
	invokespecial Mail/<init>(Ljava/lang/String;)V
	astore_1
	aload_1
	invokevirtual Mail/show()V
Label3:
Label1:
	return
.limit stack 3
.limit locals 2
.end method
