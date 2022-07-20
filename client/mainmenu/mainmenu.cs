using Godot;
using System;

public class mainmenu : Node2D
{
	// Declare member variables here. Examples:
	private Globals globals;
	private int state;

	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		state = 0;
		globals = GetNode<Globals>("/root/globals");
	}

//  // Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(float delta)
	{
		globals.update();
		if(state == 0)
		{
			return;
		}
		switch(state)
		{
			case 1:
				globals.connectTo("161.35.179.237",31337);
				state = 2;
				break;
			case 2:
				
				GetTree().ChangeScene("res://lobby/lobby.tscn");
				break;	
		}
	}

	private void _on_connectbutton_pressed()
	{
		state = 1;
	}
}
