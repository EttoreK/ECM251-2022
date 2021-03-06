public class Spock extends Jogada{
	
	public Spock(){
		super(EnumJogadas.TESOURA, EnumJogadas.PEDRA);
	}

	@Override
	public EnumJogadas getTipo(){
		return EnumJogadas.SPOCK;
	}

	@Override
	public String toString() {
		return spock;
	}

	String spock = String.join("\n",
	"                                                ",
	"                                                ",
	"                                                ",
	"                        .                       ",
	"                 ..:::::::::::..                ",
	"              .::...............::              ",
	"             ::...---.............::            ",
	"           ::....:. .:...........:..:.          ",
	"          :......-.  :............:..::         ",
	"        .:.....=.=.  -.........+  =....:.       ",
	"       .:.....:  .:  :..........  =.....:.    .:",
	"      .:......-.  -   -.......-.  -......:   .: ",
	"     .:.......-.  =   +.......:   :.......: .:  ",
	"     :........:   :   -.......:  :. :......:.   ",
	"    :..........    .  .......::  .  .......:.   ",
	"   .:..........    =   :.....:   :  ........:   ",
	"   :............   =   =.....:  ..  :........:  ",
	"  .:...........:   :   :....+   =   -........:  ",
	"  :............=    .  .:....   :   :.......... ",
	" .:............=    :  .:..-   -   :..........: ",
	" ..............=    -   :.::   :   +..........: ",
	" ..............:    .   -::   :    -..........:.",
	" :...............   .    :.   :   -.............",
	" :..............=             .   =............:",
	" :..............=            .:   :............:",
	".:..............=                ..............:",
	".:.....-=:......=                ::............:",
	".:....=   --....=                :.............:",
	".:....-    .::..=                :.............:",
	" :....:-     ::.-                :.............:",
	" :......-.    ::-                :.............:",
	" :.......-.    :=                :.............:",
	" :........:     .                :............:.",
	" ..........:                     .............: ",
	" .:........:.                    .............: ",
	"  :.........=                    .............. ",
	"  :..........-                   ............:. ",
	"   :.........:.                  ............:  ",
	"   .:.........:                  ...........:   ",
	"    :..........=.                :.........::   ",
	"    .:..........-:              .-.........:    ",
	"     ::...........=              :........:::   ",
	"      ::...........-            -........:.  :. ",
	"       :............            =.......:.    ..",
	"        ::...........           =......:.      .",
	"         ::..........           =.....:.        ",
	"          .::........           =...::          ",
	"            .:.......           =.::.           ",
	" ");
}
