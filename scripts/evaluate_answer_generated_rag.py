# coding: utf8
import torch
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer,file_utils
# print(file_utils.default_cache_path)
import pandas as pd
from tqdm import tqdm
name_file = "evaluat_dataset_2.csv"

df  = pd.read_csv(name_file, sep= "|")
df['answer_generated_phoGPT'] = None

# torch.cuda.empty_cache()
# print(torch.cuda.memory_summary(device=None, abbreviated=False))
# print(torch.cuda.current_device())
# print(torch.cuda.is_available())
model_path = "vinai/PhoGPT-4B-Chat"  

config = AutoConfig.from_pretrained(model_path, trust_remote_code=True)  
# device = 'cuda:1'
device = torch.device('cuda:1')
config.init_device = device
# config.attn_config['attn_impl'] = 'flash' # If installed: this will use either Flash Attention V1 or V2 depending on what is installed

model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.bfloat16, trust_remote_code=True).to(device)
# If your GPU does not support bfloat16:
# model = AutoModelForCausalLM.from_pretrained(model_path, config=config, torch_dtype=torch.float16, trust_remote_code=True)
model.eval()  
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

PROMPT_TEMPLATE = "### Câu hỏi: {instruction}\n### Trả lời:"  

# Some instruction examples
# instruction = "Viết bài văn nghị luận xã hội về {topic}"
# instruction = "Viết bản mô tả công việc cho vị trí {job_title}"
# instruction = "Sửa lỗi chính tả:\n{sentence_or_paragraph}"
# instruction = "Tóm tắt văn bản:\n{text}"

# instruction = "Viết bài văn nghị luận xã hội về an toàn giao thông"
# instruction = "Sửa lỗi chính tả:\nTriệt phá băng nhóm kướp ô tô, sử dụng \"vũ khí nóng\""
for index in tqdm(range(len(df))):
    example = df.iloc[index]
    question = example["question"]
    text =  example["context"]
    
    # text = """
    # Cách làm cho hoa cà phê ra đồng loạt?
    # Muốn cà phê ra hoa đồng loạt cần xác định thời điểm tưới nước cho phù hợp. Việc xác định thời điểm tưới, lượng nước tưới, 
    # phương pháp tưới tùy thuộc vào điều kiện thời tiết, loại đất, tình trạng sinh trưởng của cây. Sau thời gian khô hạn, khi 
    # thấy nụ hoa có dạng mỏ sẻ xuất hiện đầy đủ ở đốt ngoài cùng của các cành thì tiến hành tưới nước cho cà phê. Việc tưới nước 
    # đúng thời điểm lần đầu (đợt 1) và đủ lượng nước tưới sẽ quyết định đến việc ra hoa đồng loạt.
    # """
    # question ="""
    # Làm thế nào để cà phê ra hoa đồng loạt?
    # """
    # instruction = \
    # """
    #     Trả lời câu hỏi của người dùng dựa vào văn bản bên dưới theo các yêu cầu được sau đây.\n
    #     Yêu cầu: Câu trả lời phải được trích xuất thông tin hoàn toàn từ văn bản cung cấp. Giữ câu trả lời ngắn gọn và súc tích. Nếu câu hỏi không thể trả lời từ đoạn văn bản, trả về kết quả  "Tôi không thể trả lời câu hỏi này".\n
    #     Văn bản cung cấp:\n{text}\n
    #     Câu hỏi người dùng: {question}        
    # """.format_map({"text": text, "question":question})
    instruction = "Dựa vào văn bản sau đây:\n{text}\nHãy trả lời câu hỏi: {question}".format_map({"text": text, "question":question})
    # print(instruction)

    input_prompt = PROMPT_TEMPLATE.format_map({"instruction": instruction})  
    # print(input_prompt)

    input_ids = tokenizer(input_prompt, return_tensors="pt").to(device)

    outputs = model.generate(  
        inputs=input_ids["input_ids"].to(device),  
        attention_mask=input_ids["attention_mask"].to(device),  
        do_sample=True,  
        temperature=1.0,  
        top_k=50,  
        top_p=0.9,  
        max_new_tokens=1024,  
        eos_token_id=tokenizer.eos_token_id,  
        pad_token_id=tokenizer.pad_token_id  
    ).to(device) 

    response = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]

    # print(response)
    response = response.split("### Trả lời:")[1]
    df.at[index,'answer_generated_phoGPT'] = response 
    print(text)
    print("________")
    print(question)
    print("________")
    print(response)
    print("_______________________________________________________")

df[['context','question','answer_generated_phoGPT']].to_excel('answer_generated_phoChatGPT_result_of_' + name_file.replace('.csv','')+'.xlsx')
import GPUtil
del model
gpu = GPUtil.getGPUs()[1]
memoryUsed = gpu.memoryUsed
print(memoryUsed)