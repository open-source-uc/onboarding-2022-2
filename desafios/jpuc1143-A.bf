Use este interprete https://www.nayuki.io/page/brainfuck-interpreter-javascript
Lamentablemente no alcance a implementar el carry...

Primer argumento                                                                
Extraer -++++++++++++++++[---------------->,--------------------------------]   
Segundo argumento                                                               
-++++++++++++++++++++++++++++++++++++++++++++++++
[------------------------------------------------>,]  

Reflect second ->--->-<<<+[-
Next Digit >>+[->+]>>- Back <<--+[-<+]-<
Move Digit [->>+[->+]-<+< Back  +[-<+]-< ] >+<-<+     
]
Reflect first ->+<< +[-
Next Digit >>++[-->++] >> [-]-- Back +[-<+]-<
Add Digit [->>++[-->++]--<+< Back  +[-<+]-< ] >+<-<+   
]
Find LSD
+++[--->+++]->
Calculate Carry :(
Find MSD
++[-->++]>>[>>]<<<
Print +[-++++++++++++++++++++++++++++++++++++++++++++++++.<<+]
