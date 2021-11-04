package me.eza.candylandy;

@Mod(Main.ID)
public class Main {
public static final String ID = "candylandy";
    private static final Logger LOGGER = LogManager.getLogger();
    public ExampleMod() {
        MinecraftForge.EVENT_BUS.register(this);
    }
        