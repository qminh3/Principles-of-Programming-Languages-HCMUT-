.source Engine.java
.class public  Engine
.super java.lang.Object
.implements Machine
.field status Ljava/lang/String;

.method public <init>(Ljava/lang/String;)V
.var 0 is this LEngine; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is status Ljava/lang/String; from Label0 to Label1
Label2:
	aload_0
	aload_1
	putfield Engine/status Ljava/lang/String;
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LEngine; from Label0 to Label1
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

.method public start()V
.var 0 is this LEngine; from Label0 to Label1
Label0:
Label2:
	ldc "Start "
	invokestatic io/putString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public stop()V
.var 0 is this LEngine; from Label0 to Label1
Label0:
Label2:
	ldc "Stop"
	invokestatic io/putString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
