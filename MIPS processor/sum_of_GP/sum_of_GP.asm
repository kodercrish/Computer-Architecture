.data
	data: .word 0
	#data memory
		#0 --- a  $s1  0
		#1 --- r  $s2  4
		#2 --- n  $s0  8
		#3 --- answer  $s3  12
	
.text
	#la	$s7, data	#$s7 has the address value of first data memory
				#$s6 = 0 ; is always storing the value to which we have to compare n
	
	li	$v0, 5
	syscall
	sw	$v0, 0($s7)
	
	li	$v0, 5
	syscall
	sw	$v0, 4($s7)
	
	li	$v0, 5
	syscall
	sw	$v0, 8($s7)
	
	
	
	lw	$s0, 8($s7)
	bne	$s0, $s6, sigma
	
	
	sigma:
		lw	$s1, 0($s7)
		lw	$s2, 4($s7)
		lw	$s3, 12($s7)
		
		add	$s3, $s3, $s1
		sw	$s3, 12($s7)
		li	$t0, 1
		sub	$s0, $s0, $t0
		sw	$s0, 8($s7)
		
		mul	$s1, $s1, $s2
		sw	$s1, 0($s7)
		
		beq	$s0, $s6, cont
		j	sigma
		
	cont:
	
	lw	$s6, 12($s7)
	
	li	$v0, 10
	syscall
