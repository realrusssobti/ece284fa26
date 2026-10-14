// Created by prof. Mingu Kang @VVIP Lab in UCSD ECE department
// Please do not spread this code without permission 
module mac (out, A, B, format, acc, clk, reset);

parameter bw = 8;
parameter psum_bw = 16;

input clk;
input acc;
input reset;
input format;

input signed [bw-1:0] A;
input signed [bw-1:0] B;

output signed [psum_bw-1:0] out;

reg signed [psum_bw-1:0] psum_q;
reg signed [bw-1:0] a_q;
reg signed [bw-1:0] b_q;

wire [psum_bw-1:0] psum_magnitude = psum_q < 0 ? -psum_q : psum_q;
assign out = format ? {psum_q[psum_bw-1], psum_magnitude[psum_bw-2:0]} : psum_q;

// Your code goes here
always @(posedge clk) begin
	if(format) begin
		a_q <= A[bw-1] ? -$signed({1'b0, A[bw-2:0]}) : $signed({1'b0, A[bw-2:0]});
		b_q <= B[bw-1] ? -$signed({1'b0, B[bw-2:0]}) : $signed({1'b0, B[bw-2:0]});
	end else begin
		a_q <= A;
		b_q <= B;
	end
	if (reset) begin
		psum_q <= 0;
	end
	else if(acc == 1) begin
		psum_q <= psum_q + (a_q * b_q);
	end
	else begin
		psum_q <= (a_q * b_q);
	end
end


endmodule
