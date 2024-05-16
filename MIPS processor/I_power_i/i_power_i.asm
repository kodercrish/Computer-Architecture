.data

	data: .word 0, 100, 1, 0, 1, 0, 1

.text
	#la	$s7, data
	
	
	#Storing the data for instructions	
	
	#0
	li	$v0, 5
	syscall
	sw 	$v0, 0($s7)
	
	#1
	li	$v0, 5
	syscall
	sw 	$v0, 4($s7)
	
	#2#
	#li	$v0, 5
	#syscall
	#sw 	$v0, 8($s7)
	
	#3#
	#li	$v0, 5
	#syscall
	#sw 	$v0, 12($s7)
	
	#4#
	#li	$v0, 5
	#syscall
	#sw 	$v0, 16($s7)
	
	#5#
	#li	$v0, 5
	#syscall
	#sw 	$v0, 20($s7)
	
	#6#
	#li	$v0, 5
	#syscall
	#sw 	$v0, 24($s7)
	
	#main instructions
	main:
	
		loop1:
			lw 	$s4, 16($s7)
			lw 	$s0, 0($s7)
			mul	$s4, $s4, $s0
			sw 	$s4, 16($s7)
		
			lw 	$s1, 4($s7)
			lw	$s2, 8($s7)
			sub	$s1, $s1, $s2
			sw	$s1, 4($s7)
		
			lw	$s3, 12($s7)
			beq	$s1, $s3, cont1
			j	loop1
			
		cont1:
		
		lw	$s5, 20($s7)
		lw	$s4, 16($s7)
		add	$s5, $s5, $s4
		sw	$s5, 20($s7)
		
		lw	$s6, 24($s7)
		addi	$s4, $s6, 0
		sw	$s4, 16($s7)
		
		lw	$s0, 0($s7)
		lw	$s2, 8($s7)
		sub	$s0, $s0, $s2
		sw	$s0, 0($s7)
		sw	$s0, 4($s7)
		
		lw	$s3, 12($s7)
		beq	$s3, $s0, cont2
		j	main
		
		cont2:
		
		lw	$s6, 20($s7)
		
		li	$v0, 10
		syscall
