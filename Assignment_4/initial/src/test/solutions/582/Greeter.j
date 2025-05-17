.source Greeter.java
.class public  Greeter
.super java.lang.Object
.field name Ljava/lang/String;

.method public <init>(Ljava/lang/String;)V
.var 0 is this LGreeter; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is name Ljava/lang/String; from Label0 to Label1
Label2:
	aload_0
	aload_1
	putfield Greeter/name Ljava/lang/String;
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LGreeter; from Label0 to Label1
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

.method public greet(I)V
.var 0 is this LGreeter; from Label0 to Label1
Label0:
.var 1 is times I from Label0 to Label1
Label2:
.var 2 is i I from Label2 to Label3
	iconst_0
	istore_2
Label6:
	iload_2
	iload_1
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
Label9:
	aload_0
	getfield Greeter/name Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
Label10:
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label6
Label5:
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method
