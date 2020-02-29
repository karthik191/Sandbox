module sync_wr2rd #(parameter width =8, depth = 7)
(input[depth:0] wptr,input clk_out,reset,flush, output reg[depth:0] w2rsync_ff2, output reg syn_flush);
reg [depth:0] w2rsync_ff1;
reg sync_flush1;
always @(posedge clk_out, negedge reset)
begin
	if(!reset)
	begin
		w2rsync_ff2 <= 0 ;
		w2rsync_ff1 <= 0 ;		
	end
	else
	begin
		w2rsync_ff1 <= wptr ;
		w2rsync_ff2 <= w2rsync_ff1;
	end
end
always @(posedge clk_out, negedge reset)
begin
if(!reset)
	syn_flush<=0;
else
begin
		sync_flush1 <= flush ;
		syn_flush<= sync_flush1;		
end
end
endmodule

