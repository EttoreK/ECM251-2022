public class Pedra extends Jogada{

	public Pedra(){
		super(EnumJogadas.TESOURA, EnumJogadas.LAGARTO);
	}

	@Override
	public EnumJogadas getTipo(){
		return EnumJogadas.PEDRA;
	}

	@Override
	public String toString() {
		return pedra;
	}

	String pedra = String.join("\n",
"                -              .                ",
"                :. .:::::::::...                ",
"                :--:.........:--.               ",
"             .:-:...............:-..            ",
"            :::...................::.           ",
". .        -:.......................:-          ",
".:..     .::.........................::.        ",
"  :-.   .:.............................-.       ",
" ::--  .-..............::::...:.........-.      ",
"   ..:::..............-:  .   .::........:      ",
"      -..............=          -........:-     ",
"     ::.............:.     .--:..:........::    ",
"    .-.............::          =-:.........:.   ",
"    :..............-             :.........::   ",
"   .:.............-            :::-.........-   ",
"   ::............-               :.-........::  ",
"   -............::                +=.........-  ",
"  .:............:                 .::........:. ",
"  -.............=                   :.........: ",
"  -............:.                   =.........: ",
"  -............=                    -.........: ",
" .-............=                     -........: ",
" .:.............                     +........: ",
" .:...........-.                     =........: ",
":-:...........-                      =........: ",
" .:..........-.                     -:........: ",
" .-........:=                      .:.........: ",
"  -.....:-.:                       -:.........: ",
"  -...-=                         .-...........: ",
"  :-:=                          :-...........:: ",
"   :                           -:............-  ",
"   :                          :..............-  ",
"   .                        .:..............:.  ",
"    .                      .:...............:   ",
"    .                     .-...............:.   ",
"     :                  :::................:    ",
"      .               .=..................-     ",
"      .             ..-..................:.     ",
"       :          .-:...................::      ",
"        :       .=.....................::       ",
"         .    :-:.....................::        ",
"          ...=.......................-.         ",
"           .-:.....................::           ",
"             .::.................:-.            ",
"               :--............:--.              ",
"                 .:::::::::::::.                ",
"                      .....                     ",
"            ...               ...               ",
" ");
}
