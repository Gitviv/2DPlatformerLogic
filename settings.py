LEVEL_MAP = [ 
	'    C       C       C       C	        C          C             C     ',
	'                            	 E               E                     ',
	'        L       C      L    XXWXX      L  L   XXXXXX        C         ',
	'       XXWX           XX    	       XXXXXX                          ',
	'L  P           L          L 	   L               L E                 ',
	'XXXXX         XX         XX 	 XWX              XXXXXXX     E        ',
	' XXXX      EXX    L         	                            XXXXX      ',
	' XX    XWXXXX    XX  XX    	XXXX   XXXXXX                      E   ',
	'       X  XXXX    XX  XXX   	  XX                     L  L    XXXX  ',
	'    XXXX  XXXXXX  XX  XXXX  	        E    E     E    XXXXXX         ',
	'XXXXXXXX  XXXXXX  XX  XXXX  XXXXX    XXXXXXXXXXXXXXX                  '
]
# W=fake block, X=real block, L=palm, P=player, C=Cloud, E=enemy

sizes = {
    "TILE_SIZE" : 64,
    "SCREEN_WIDTH" : 1280,
    "SCREEN_HEIGHT" : 720
}

# colors 
BG_COLOR = '#96b9f2'

# camera
CAMERA_BORDERS = {
	'left': 300,
	'right': 300,
	'top':250,
	'bottom': 250
}