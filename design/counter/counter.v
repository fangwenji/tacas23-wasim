module counter(input wire clk, input wire rst, output reg [3:0] cnt);

always @(posedge clk) begin
  if (rst)
    cnt <= 0;
  else begin
    if (cnt == 10)
      cnt <= 0;
    else  
      cnt <= cnt + 1;
  end
end

assert property (cnt < 12);

endmodule

