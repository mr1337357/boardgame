using Godot;
using System;
using System.Text;
using System.Net;
using System.Net.Sockets;

public class Globals : Node
{

	public UdpClient serv_connection = null;
	
	public enum ConnectionState
	{
		None,
		Started,
		Waiting,
		Idle
	}
	
	public ConnectionState state {get;private set;}
	
	public Globals() : base()
	{
		serv_connection = null;
		state = ConnectionState.None;
	}
	
	public void connectTo(string host,int port)
	{
		if(state == ConnectionState.None)
		{
			serv_connection = new UdpClient();
			serv_connection.Connect(host,port);
		}
		state = ConnectionState.Started;
		
	}
	public void update()
	{
		switch(state)
		{
			case ConnectionState.None:
				break;
			case ConnectionState.Started:
				Byte[] sendBytes = Encoding.ASCII.GetBytes("Boardgame?");
				serv_connection.Send(sendBytes, sendBytes.Length);
				state = ConnectionState.Waiting;
				break;
			case ConnectionState.Waiting:
				if(serv_connection.Available > 0)
				{
					if(System.Text.Encoding.ASCII.GetString(serv_connection.Receive()) == "Boardgame")
					{
						state = ConnectionState.Idle;
					}
				}
			default:
				break;
		}
	}
	
}
