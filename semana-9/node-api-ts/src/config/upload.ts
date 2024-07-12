import multer from "multer";
import multerS3 from "multer-s3";
import s3 from "./s3";
import type { Request } from "express";

const upload = multer({
  storage: multerS3({
    s3,
    bucket: process.env.AWS_S3_BUCKET_NAME as string,
    metadata: (_req: Request, file, cb) => {
      cb(null, {
        fieldName: file.fieldname,
      });
    },
    key: (_req: Request, file, cb) => {
      cb(null, `${Date.now()}-${file.originalname}`);
    },
  }),
});

export default upload;
