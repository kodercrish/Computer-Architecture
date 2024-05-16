.data
	data: .word 0
.text
	#la 	$s7, data
	
	li 	$v0, 5
	syscall
	sw	$v0, 0($s7)
	lw	$s3, 0($s7)
	li	$s4, 3
	
	li 	$t0, 0
	li	$t1, 0
	li 	$t2, 1
	
	loop:
		addi	$s0, $t1, 0
		addi	$s1, $t2, 0
		add	$s2, $t0, $t1
		add	$s2, $s2, $t2
		
		addi	$t0, $s0, 0
		addi	$t1, $s1, 0
		addi	$t2, $s2, 0
		
		addi	$s4, $s4, 1
		
		beq	$s4, $s3, cont
		j	loop
	cont:
		addi	$s6, $s2, 0
		
		li	$v0, 10
		syscall
		
		