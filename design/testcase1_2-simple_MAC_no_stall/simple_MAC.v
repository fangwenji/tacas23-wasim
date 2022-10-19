module test(input wire clk, input wire rst, input wire [3:0] w,
    input wire [3:0] reg_init,
    output wire [3:0] out);

reg [3:0] stage1;
reg [3:0] stage2;
reg [3:0] stage3;
reg tag0;
reg tag1;
reg tag2;
reg tag3;
reg tag4;


reg wen_stage1, wen_stage2, wen_stage3;


assume property (wen_stage3 == 1); 
assume property (~(wen_stage2 & ~wen_stage1)); 

always @(posedge clk) begin
  if(rst) begin 
    // stage1 <= 0;
    // stage2 <= 0;
    // stage3 <= w;
    // {wen_stage1, wen_stage2, wen_stage3} <= 1;
    {tag4,tag3,tag2,tag1,tag0} <= 1;
  end else begin
        tag0 <= 1'b0; 
        tag1 <= tag0;
        tag2 <= tag1;
        tag3 <= tag2;
        tag4 <= tag3;

        wen_stage1 <= wen_stage3;
        wen_stage2 <= wen_stage1;

        stage1 <= 
          wen_stage1 ? stage1 * 2 + 1 : 
        //wen_stage2 ? stage2 :
          wen_stage3 ? stage3 : stage3;

        stage2 <= stage1 * 2 + 1 ;
        stage3 <= wen_stage2 ? stage2 : stage3;
  end
end

assign out = stage3;

reg [3:0] reg_v;
always @(posedge clk) begin
  //reg_v <= reg_init;
  if(rst)
    reg_v <= reg_init;
  else
    reg_v <= reg_v;
end

reg [3:0] reg_v_comp;
always @(posedge clk) begin
  // if((tag2 && !tag3))
    reg_v_comp <= reg_v *2 + 1;
end


wire [3:0] reg_v_mul2_plus1 = reg_v*2+1;

assume property (~(tag2 ) || (reg_v == stage3));
assert property (~(tag3 ) || (reg_v_comp == stage3));


endmodule

