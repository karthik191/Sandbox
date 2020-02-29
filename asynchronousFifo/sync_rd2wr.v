module sync_rd2wr #(parameter width =8, depth = 7)
(input[depth:0] rptr,input clk_in,reset,flush,input[31:0] data_in, output reg[depth:0] r2wsync_ff2,output reg[31:0] temp_data_in);
reg [depth:0] r2wsync_ff1;
reg [31:0] temp4;
always @(posedge clk_in, negedge reset)
begin
	if(!reset)
	begin
		r2wsync_ff2 <= 0 ;
		r2wsync_ff1 <= 0 ;		
	end
	else
	begin    //$display("b4syn r2w",rptr );
		r2wsync_ff1 <= rptr ;
		r2wsync_ff2 <= r2wsync_ff1;//$display("aftr syn r2w",r2wsync_ff2 );
	end
end
always @ (posedge clk_in or negedge reset)
begin
	if(!reset)
		temp_data_in<=32'h0;
	else
	begin
		temp4<=data_in;
		temp_data_in<=temp4;
	end
end
endmodule

