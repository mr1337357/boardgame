using Godot;
using System;

public class lobby : Node2D
{
	Node globals;
	// Declare member variables here. Examples:
	// private int a = 2;
	// private string b = "text";
	private int lobbystate;

	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		lobbystate = 0;
		globals = GetNode<Node>("/root/globals");
		
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(float delta)
	{
		
	}
}
