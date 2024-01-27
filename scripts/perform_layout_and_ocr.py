import layoutparser as lp
import argparse
import cv2


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--image_file", dest="image_file")
    parser.add_argument("--layout_model_url", dest="layout_model_url")
    parser.add_argument("--ocr_model_url", dest="ocr_model_url")
    parser.add_argument("--layout_output", dest="layout_output")
    parser.add_argument("--ocr_output", dest="ocr_output")
    parser.add_argument("--languages", nargs="+", dest="languages", default=["spa"])
    args = parser.parse_args()
    
    layout_model = lp.models.Detectron2LayoutModel(
        args.layout_model_url
    )
    ocr_agent = lp.TesseractAgent(languages=args.languages) 
    image = cv2.imread(args.image_file)
    layout = layout_model.detect(image)
    
    with open(args.ocr_output, "wt") as ofd:
        for block in layout:
            segment_image = block.pad(left=15, right=15, top=15, bottom=15).crop_image(image)
            text = ocr_agent.detect(segment_image)            
            ofd.write(text)

    im = lp.draw_box(image, layout, box_width=3)
    im.save(args.layout_output)
