.source Book.java
.class public  Book
.super java.lang.Object
.implements Printable
.field title Ljava/lang/String;

.method public <init>(Ljava/lang/String;)V
.var 0 is this LBook; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is title Ljava/lang/String; from Label0 to Label1
Label2:
	aload_0
	aload_1
	putfield Book/title Ljava/lang/String;
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LBook; from Label0 to Label1
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

.method public print()V
.var 0 is this LBook; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Book/title Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
