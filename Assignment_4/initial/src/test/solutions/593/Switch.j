.source Switch.java
.class public  Switch
.super java.lang.Object
.implements Toggle
.field state Z

.method public <init>(Z)V
.var 0 is this LSwitch; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is state Z from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield Switch/state Z
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LSwitch; from Label0 to Label1
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

.method public isOn()Z
.var 0 is this LSwitch; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Switch/state Z
	ireturn
Label3:
Label1:
.limit stack 1
.limit locals 1
.end method
