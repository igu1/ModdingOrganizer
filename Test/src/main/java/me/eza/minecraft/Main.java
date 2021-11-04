package me.eza.minecraft;

@Mod(Main.ID)
public class Main {
public static final String ID = "minecraft";
    private static final Logger LOGGER = LogManager.getLogger();
    public ExampleMod() {
        MinecraftForge.EVENT_BUS.register(this);
    }
        