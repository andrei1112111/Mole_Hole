asect 0xF3
	IO:
asect 0x00

start:
	
	ldi r0,IO
	ldi r1,0
    # your code here
    do
		ld r0,r1

		tst r1
	until pl
		
	if
		tst r1
	is z
		 br start
	fi
	
	ldi r2, A
	st r2, r1
	
	ldi r0,res
	ld r0,r2
	ldi r1, B
	st r1, r2
	
	# End of Init
	
	ldi r0, A
	ld r0,r1
	ldi r0,B
	ld r0,r2
	
	ldi r0,0
	add r1,r2	
	
	if
	is cs
		inc r0
	fi
	
	ldi r1,res
	st r1,r2
	inc r1
	ld r1,r3
	add r0,r3
	st r1,r3
	
	ldi r1,res
	ld r1,r2 # Младший разряд числа (16-тиричная СЧ)
	
	ldi r1,0
	while 
		ldi r0, 0x0a
		move r0,r3
		sub r2, r3
	stays cs
		sub r2,r0
		inc r1
		move r0,r2
	wend
	# В r1 Лежит количество десятков
	# В r2 Лежат единицы от младшего разряда
		

	ldi r0, one
	st r0,r2
	# Сразу поработали с единицами и записали их
	
	move r1,r2
	
	ldi r1,0
	while 
		ldi r0, 0x0a
		move r0,r3
		sub r2, r3
	stays cs
		sub r2,r0
		inc r1
		move r0,r2
	wend
	
	# В r1 Лежат сотни от первого младшего разряда
	# В r2 Лежат десятки от младшего разряда
	
	ldi r0, hund
	st r0,r1
	inc r0
	st r0, r2
	# Записали десятки и сотни от младшего разряда
	
	
	
	# В r3 лежит число из старшего разряда
	
	while
			ldi r1,res
			inc r1
			ld r1,r3 # Старший разряд числа (16-тиричная СЧ)
			tst r3
	stays nz
		
		ldi r0, one
		ld r0, r1 # Загрузили единицы
		ldi r2, 0x06
		add r2,r1
		
		if
			ldi r2, 0x0a
			move r2,r3
			sub r1,r3
		is cs
			sub r1,r2
			st r0,r2 # Загрузили обновленные единицы
			 
			ldi r0,ten
			ld r0,r1
			inc r1
			st r0,r1	# Прибавили 1 к десяткам
		else
			st r0,r1
		fi
		
		ldi r0,ten
		ld r0,r1
		ldi r2,0x05
		add r2,r1
		
		if
			ldi r2, 0x0a
			move r2,r3
			sub r1,r3
		is cs
			sub r1,r2
			st r0,r2 # Загрузили обновленные десятки
			 
			ldi r0,hund
			ld r0,r1
			inc r1
			st r0,r1	# Прибавили 1 к сотням
		else
			st r0,r1			
		fi
		
		ldi r0,hund
		ld r0,r1
		ldi r2,0x02
		add r2,r1
		st r0,r1
		
		dec r3
		
		ldi r0,res
		inc r0
		st r0,r3
		
	wend
	
	ldi r0, hund
	ld r0,r0
	ldi r1,0xf0
	st r1,r0
	ldi r0,ten
	ld r0,r0
	ldi r1,0xf1
	st r1,r0
	ldi r0,one
	ld r0,r0
	ldi r1,0xf2
	st r1,r0
	
	
	
	br start
	
	
	
A: ds 1
B: ds 1

res: ds 2
hund: ds 1
ten: ds 1
one: ds 1

end